#!/usr/bin/python

from paddlespeech.cli.asr.infer import ASRExecutor

asr = ASRExecutor()
result = asr(audio_file="录音.wav", force_yes=True)
print(result)