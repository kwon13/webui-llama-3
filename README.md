# webui-llama-3
# 가상환경 세팅
```
python3 -m venv .venv
. .venv/bin/activate
```

# llama cpp 설치 
(https://github.com/ggerganov/llama.cpp)  
```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
pip install -r ./requirements.txt
```

# llama 모델을 돌리기 위해서는 llama-cpp-python 설치가 필요 
(https://github.com/abetlen/llama-cpp-python)  
`pip install llama-cpp-python`

# 모델 설치 
(https://huggingface.co/models 에서 다양한 모델을 받을 수 있음.)  
1. huggingface에서 모델 불러와서 설치
2. `.gguf` 형식으로 모델 파일 변경
3. 변경된 `.gguf` 파일을 더 작은 사이즈로 모델 quantization 수행 (필수가 아니기 때문에 model_prepare.py 파일에서 주석처리로 건너뛸 수 있습니다.)
```
pip install huggingface_hub
python3 model_quantization.py
```

# webui 설치 
(https://github.com/oobabooga/text-generation-webui)  
```
git clone https://github.com/oobabooga/text-generation-webui.git
cd text-generation-webui
```
위에서 다운받은(혹은 퀀타이즈 한)모델의 `.gguf` 파일을 `text-generation-webui/models` 폴더로 이동시킵니다.  
**for macos**
```
pip install -r requirements_apple_silicon.txt
sh start_macos.sh 
```

아래 링크 접속
http://localhost:7860/?__theme=dark
