
from paddlespeech.server.bin.paddlespeech_client import TextClientExecutor

textclient_executor = TextClientExecutor()
res = textclient_executor(
    input="我认为跑步最重要的就是给我带来了身体健康",
    server_ip="127.0.0.1",
    port=8090,)