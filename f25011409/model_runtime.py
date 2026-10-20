"""Shared loading and generation functions for the CLI and web interface."""

from functools import lru_cache
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


ROOT = Path(__file__).resolve().parent
MODEL_PATH_FILE = ROOT / "model_path.txt"


def resolve_model_path() -> str:
    if not MODEL_PATH_FILE.exists():
        raise FileNotFoundError(
            "Model path is missing. Run `python download_model.py` before starting the app."
        )
    model_path = Path(MODEL_PATH_FILE.read_text(encoding="utf-8").strip())
    if not (model_path / "config.json").exists():
        raise FileNotFoundError(
            f"Model files were not found at {model_path}. Run `python download_model.py` again."
        )
    return str(model_path)


@lru_cache(maxsize=1)
def load_model():
    model_path = resolve_model_path()
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype="auto",
        device_map="auto" if torch.cuda.is_available() else "cpu",
        trust_remote_code=True,
    )
    model.eval()
    return tokenizer, model


def generate_reply(messages: list[dict[str, str]], max_new_tokens: int = 512) -> str:
    tokenizer, model = load_model()
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.inference_mode():
        output = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id,
        )
    new_tokens = output[0, inputs["input_ids"].shape[1] :]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
