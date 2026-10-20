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

网页聊天运行 `streamlit run web_app.py`，再打开终端显示的本机地址，通常为 `http://localhost:8501`。首次运行前需要下载模型；PyTorch 请按设备选择对应安装版本。

## 自动发布

`Jenkinsfile` 提供依赖安装和 Python 语法检查示例；实际部署需另行配置测试服务器、凭据与发布步骤。模型下载和推理尚未在本机实测，见 [0920 作业报告](./0920作业.md)。# f25011409 开源模型部署与调用

基于 0920 课程示例，在本机下载并调用 Qwen3-0.6B，提供命令行与 Streamlit 网页聊天。模型权重不提交到仓库。

## 环境
Windows 10/11，Python 3.10-3.12。CPU 可运行；本机 RTX 5060 为 8GB 显存，使用较小的 Qwen3-0.6B。首次下载需要网络和数 GB 磁盘空间。

## 安装和运行

```powershell
cd $HOME\ai-opensource-practice-course\demo_1
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python download_model.py
python qwen01.py
streamlit run qwen02.py
```

访问 Streamlit 输出的本机地址，通常为 http://localhost:8501。先用 qwen01.py 验证终端推理，再验证网页聊天。NVIDIA GPU 的 PyTorch 按官方安装选择器选择适合本机的 CUDA 构建。

## 自动发布
课程 demo_1/Jenkinsfile 示范检出代码、Docker Compose 构建、部署和健康检查；deploy.sh 可手动构建和启动。真正部署前需配置测试服务器、凭据和发布命令。模型下载和推理尚未在本机实测，详见 [0920 作业报告](0920作业.md)。