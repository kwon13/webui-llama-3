import subprocess
from huggingface_hub import snapshot_download

# 모델 웨이트 다운로드
model_id="fiveflow/KoLlama-3-8B-Instruct"
snapshot_download(repo_id=model_id, local_dir="KoLlama-3-8B-Instruct",
                  local_dir_use_symlinks=False, revision="main")

# 모델 파일 .gguf로 변환
command = "python3 llama.cpp/convert.py KoLlama-3-8B-Instruct --outfile KoLlama-3-8B-Instruct-v0.1.gguf --outtype f16 --vocab-type bpe"
subprocess.run(command.split(), check=True)

# 모델 퀀타이즈 수행 (필수 아님)
command = "llama.cpp/quantize ../webui-llama-3/KoLlama-3-8B-Instruct-v0.1.gguf ../webui-llama-3/ggml-model-Q4_K.gguf Q4_K"
subprocess.run(command.split(), check=True)
