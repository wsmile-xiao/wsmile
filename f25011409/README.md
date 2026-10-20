# Qwen3-0.6B 本地部署与调用

学号：f25011409

依据 0920 课程示例，使用 ModelScope 下载 Qwen3-0.6B，通过 Transformers 在本机推理，并提供终端聊天和 Streamlit 网页聊天。提问和生成均在本机运行；模型权重只保存在本地，不提交到 Git。

本项目沿用课程要求的 Qwen3-0.6B，不直接照搬参考仓库针对 RTX 5070 Ti 16GB 的 Qwen2.5-7B、量化及 Gradio 配置。本机检测到 RTX 5060 8GB 显存；实际推理是否可用仍需本机验证。

## 环境

- Windows 10/11，Python 3.10-3.12
- 首次下载需要网络和数 GB 可用空间
- CPU 可推理但较慢；NVIDIA GPU 需安装匹配的 PyTorch CUDA 版本

## 安装与运行

从仓库根目录进入本项目目录：

```powershell
cd .\f25011409
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

按设备从 [PyTorch 官方安装选择器](https://pytorch.org/get-started/locally/) 安装 PyTorch，然后下载模型：

```powershell
python download_model.py
```

终端聊天：

```powershell
python chat_cli.py
```

输入 `/reset` 清空对话，输入 `/exit` 退出。网页聊天：

```powershell
streamlit run web_app.py
```

打开 Streamlit 输出的本机地址，通常为 `http://localhost:8501`。

## 项目文件

- `download_model.py`：从 ModelScope 下载 Qwen3-0.6B，并记录本地快照路径
- `model_runtime.py`：加载 tokenizer/模型并生成回答，CLI 与网页共用
- `chat_cli.py`：多轮终端聊天
- `web_app.py`：Streamlit 聊天界面
- `requirements.txt`：Python 依赖；PyTorch 根据本机设备单独安装
- `Jenkinsfile`：依赖安装和 Python 语法检查示例；部署步骤需配置测试服务器后再启用
- `0920作业.md`：第 1 项开源模型部署调用方案和第 2 项自动发布方式调研

## 验证状态

Python 文件已通过语法编译检查。模型下载、依赖安装、GPU/CPU 推理和网页交互尚未在目标机器完成验证；请运行后在 `0920作业.md` 补充实际结果，不要将计划步骤记为成功。

## 参考

- 课程仓库：<https://gitcode.com/nicezack/ai-opensource-practice-course>
- ModelScope 教程：<https://www.modelscope.cn/posts/1964>
- 参考项目（参考目录和说明组织方式）：<https://gitcode.com/leishijia/920>
