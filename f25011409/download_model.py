from pathlib import Path; from modelscope.hub.snapshot_download import snapshot_download
root=Path(__file__).resolve().parent; cache=root/'models'; cache.mkdir(exist_ok=True)
path=snapshot_download('Qwen/Qwen3-0.6B',cache_dir=str(cache)); (root/'model_path.txt').write_text(str(Path(path).resolve()),encoding='utf-8'); print(f'Model downloaded to: {path}')