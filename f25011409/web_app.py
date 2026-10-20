"""Streamlit web chat for the locally downloaded Qwen3 model."""

import streamlit as st

from model_runtime import generate_reply


st.set_page_config(page_title="Qwen3 本地聊天", page_icon="Q", layout="centered")
st.title("Qwen3 本地聊天")
st.caption("模型在本机加载。首次启动前请先运行模型下载脚本。")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "你是一个准确、清晰的中文助手。"}
    ]

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("输入问题"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            with st.spinner("模型正在生成回答…"):
                answer = generate_reply(st.session_state.messages)
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as exc:
            st.error(f"模型调用失败：{exc}")
            st.session_state.messages.pop()

if st.button("清空对话"):
    st.session_state.messages = st.session_state.messages[:1]
    st.rerun()
