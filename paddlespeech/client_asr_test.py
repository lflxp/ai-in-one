
import requests
import base64
import json

def paddlespeech_request(url, data):
    """ 
    构造PaddleSpeech所需的post请求
    """

    res = requests.post(
        url=url,
        data=json.dumps(data)
    )

    if res.status_code == 200:
        res = res.json()
    else:
        print("请求失败，错误代码：", res.status_code)
        res = None
    return res

wav_file = "./zh.wav"
asr_url = "http://127.0.0.1:8090/paddlespeech/asr"

# 将wav转成base64
with open(wav_file, 'rb') as f:
    base64_bytes = base64.b64encode(f.read())
    base64_string = base64_bytes.decode('utf-8')

data = {
    "audio": base64_string,
    "audio_format": "wav",
    "sample_rate": 16000,
    "lang": "zh_cn",
    "punc": 0
}

res = paddlespeech_request(asr_url, data)

print(res)