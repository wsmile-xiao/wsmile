"""Download Qwen3-0.6B from ModelScope into the local models directory."""

import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MODEL_CACHE = ROOT / "models"
MODEL_CACHE.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MODELSCOPE_HOME", str(ROOT / ".modelscope"))
os.environ.setdefault("MODELSCOPE_CACHE", str(MODEL_CACHE))

from modelscope.hub.snapshot_download import snapshot_download


def main() -> None:
    print("Downloading Qwen/Qwen3-0.6B. The first download may take a while.")
    model_path = snapshot_download(
        model_id="Qwen/Qwen3-0.6B",
        cache_dir=str(MODEL_CACHE),
    )
    resolved_path = str(Path(model_path).resolve())
    (ROOT / "model_path.txt").write_text(resolved_path, encoding="utf-8")
    print(f"Model downloaded to: {resolved_path}")


if __name__ == "__main__":
    main()
