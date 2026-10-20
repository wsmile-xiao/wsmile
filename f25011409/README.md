# f25011409 开源模型部署与调用

基于 0920 课程示例，在本机部署 Qwen3-0.6B，提供命令行和 Streamlit 网页聊天。模型权重只保存在本地，不提交到仓库。

## 环境
Windows 10/11、Python 3.10-3.12。支持 CPU；NVIDIA GPU 可加速。本机 RTX 5060，8GB 显存。首次下载模型需要网络和数 GB 磁盘空间。

## 安装与运行
在本目录 PowerShell 执行：
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python download_model.py
python chat_cli.py
```
网页聊天运行 `streamlit run web_app.py`，再打开终端显示的本机地址（通常为 http://localhost:8501）。PyTorch 请按设备选择对应安装版本。

## 自动发布
`Jenkinsfile` 提供依赖安装和 Python 语法检查示例，实际部署需另行配置测试服务器、凭据和发布步骤。模型下载和推理尚未在本机实测，见 [0920 作业报告](./0920作业.md)。