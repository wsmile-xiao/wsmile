"""Interactive terminal chat with the locally downloaded Qwen3 model."""

from model_runtime import generate_reply


def main() -> None:
    print("Qwen3-0.6B local chat. Type /exit to quit, /reset to clear history.")
    messages: list[dict[str, str]] = [
        {"role": "system", "content": "你是一个准确、清晰的中文助手。"}
    ]
    while True:
        try:
            prompt = input("\n你：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n已退出。")
            break
        if not prompt:
            continue
        if prompt.lower() in {"/exit", "/quit"}:
            break
        if prompt.lower() == "/reset":
            messages = messages[:1]
            print("对话历史已清空。")
            continue
        messages.append({"role": "user", "content": prompt})
        try:
            answer = generate_reply(messages)
        except Exception as exc:
            messages.pop()
            print(f"模型调用失败：{exc}")
            continue
        messages.append({"role": "assistant", "content": answer})
        print(f"\nQwen：{answer}")


if __name__ == "__main__":
    main()
