# 环境准备

* WSL2
* Win10
* python3 和 pip3

# 安装 

- python -m pip install paddlepaddle==2.3.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
- pip install paddlespeech
- sudo apt-get install libsndfile1
- python test.py
- paddlespeech asr --lang zh --input zh.wav

# 音频格式切换

- sox 录音.m4a --rate 16k --bits 16 --channels 1 output_audio.wav

# 参考

- https://aistudio.baidu.com/aistudio/projectdetail/4379979
- https://blog.csdn.net/m0_55837832/article/details/119651362
- https://aistudio.baidu.com/aistudio/projectoverview/public
- https://aistudio.baidu.com/aistudio/course/introduce/25130?directly=1&shared=1
- https://aistudio.baidu.com/aistudio/projectdetail/4692119?channelType=0&channel=0
- https://aistudio.baidu.com/aistudio/newbie