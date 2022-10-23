from paddlespeech.server.bin.paddlespeech_client import TTSClientExecutor
import json

ttsclient_executor = TTSClientExecutor()
res = ttsclient_executor(
    input="您好，欢迎使用百度飞桨语音合成服务。",
    server_ip="127.0.0.1",
    port=8090,
    spk_id=0,
    speed=1.0,
    volume=1.0,
    sample_rate=0,
    output="./output_tts.wav")

response_dict = res.json()
print(response_dict["message"])
print("Save synthesized audio successfully on %s." % (response_dict['result']['save_path']))
print("Audio duration: %f s." %(response_dict['result']['duration']))