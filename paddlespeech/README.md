# 环境准备

* WSL2
* Win10
* python3 和 pip3

# 安装 

- python -m pip install paddlepaddle==2.3.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
- pip install paddlespeech
- sudo apt-get install libsndfile1
- python -m pip install moviepy auditok
- python test.py
- paddlespeech asr --lang zh --input zh.wav

## macos 安装

- python 3.10.7
- pip install paddlespeech== 是查询版本
- paddlepaddle==2.3.2
- paddleaudio==1.0.1
- paddlespeech==1.0.1
- onnx==1.9.0
- onnxruntime==1.12.0

## 校验

pyenv python 3.9.2没有问题 是安装的版本问题

> python -c "from paddlespeech.cli.asr.infer import ASRExecutor"

## 切分大文件 pypinyin_dict.large_pypinyin.py

切分成两个文件，然后用`from .other import other_data`

```python
from pypinyin import load_phrases_dict
from .other import other_data

def load():
    phrases_dict.update(other_data)
    load_phrases_dict(phrases_dict)
```

# tts 语音合成

- paddlespeech tts --am fastspeech2_aishell3 --voc hifigan_aishell3 --input "感谢灵犀不的办卡" --spk_id 16 --output output_zh.wav

# 一键部署

- git clone -b r1.2 https://gitee.com/paddlepaddle/PaddleSpeech
- pip install uvicorn==0.18.3 
  - [BUG #2565](https://github.com/PaddlePaddle/PaddleSpeech/issues/2565)
- paddlespeech_server start --config_file ./paddlespeech/server/conf/application.yaml

## asr

- paddlespeech_client asr --server_ip 127.0.0.1 --port 8090 --input ./zh.wav

## tts

- paddlespeech_client tts --server_ip 127.0.0.1 --port 8090 --input "您好，欢迎使用百度飞桨语音合成服务。" --output output_tts.wav
- paddlespeech_client cls --server_ip 127.0.0.1 --port 8090 --input ./zh.wav
- paddlespeech_client vector --task spk  --server_ip 127.0.0.1 --port 8090 --input ./zh.wav 

## 标点恢复

- paddlespeech_client text --server_ip 127.0.0.1 --port 8090 --input "我认为跑步最重要的就是给我带来了身体健康"

# 音频格式切换

- sox 录音.m4a --rate 16k --bits 16 --channels 1 output_audio.wav

# 虚拟主播

- git clone https://gitee.com/xiejiehang/PaddleBoBo.git -b develop
- pip install ppgan paddlespeech
- python create_virtual_human.py --config default.yaml
  - ImportError: libGL.so.1: cannot open shared object file: No such file or directory
    - https://blog.csdn.net/qq_50195602/article/details/124188467
    - pip install opencv-python-headless

# 为 WSL 启用图形化及音频支持

- https://blog.sandtears.com/2020/02/27/wsl-gui-audio-support.html

# WIKI

- https://github.com/PaddlePaddle/PaddleSpeech/wiki/PaddleSpeech-Server-RESTful-API

# 参考

- https://aistudio.baidu.com/aistudio/projectdetail/4379979
- https://blog.csdn.net/m0_55837832/article/details/119651362
- https://aistudio.baidu.com/aistudio/projectoverview/public
- https://aistudio.baidu.com/aistudio/course/introduce/25130?directly=1&shared=1
- https://aistudio.baidu.com/aistudio/projectdetail/4692119?channelType=0&channel=0
- https://aistudio.baidu.com/aistudio/newbie
- https://github.com/PaddlePaddle/PaddleSpeech/wiki/PaddleSpeech-Server-RESTful-API