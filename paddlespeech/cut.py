from paddlespeech.cli.asr.infer import ASRExecutor
# import csv
import moviepy.editor as mp
import auditok
import os
import paddle
# from paddlespeech.cli import ASRExecutor, TextExecutor
import soundfile
# import librosa
import warnings

warnings.filterwarnings('ignore')

# 引入auditok库
import auditok
# 输入类别为audio
# https://www.xiaoyuanjiu.com/108467.html
# def qiefen(path, ty='audio', mmin_dur=0.2, mmax_dur=4, mmax_silence=0.3, menergy_threshold=55):
# def qiefen(path, ty='audio', mmin_dur=1, mmax_dur=100000, mmax_silence=1, menergy_threshold=50):
# def qiefen(path, ty='audio', mmin_dur=1, mmax_dur=100000, mmax_silence=3, menergy_threshold=55):
def qiefen(path, ty='audio', mmin_dur=1, mmax_dur=100000, mmax_silence=0.5, menergy_threshold=55):
    audio_file = path
    audio, audio_sample_rate = soundfile.read(
        audio_file, dtype="int16", always_2d=True)

    audio_regions = auditok.split(
        audio_file,
        min_dur=mmin_dur,  # minimum duration of a valid audio event in seconds
        max_dur=mmax_dur,  # maximum duration of an event
        # maximum duration of tolerated continuous silence within an event
        max_silence=mmax_silence,
        energy_threshold=menergy_threshold,  # threshold of detection
        large_file=True
    )

    for i, r in enumerate(audio_regions):
        # Regions returned by `split` have 'start' and 'end' metadata fields
        print(
            "Region {i}: {r.meta.start:.3f}s -- {r.meta.end:.3f}s".format(i=i, r=r))

        epath = ''
        file_pre = str(epath.join(audio_file.split('.')[0].split('/')[-1]))

        mk = 'change'
        if (os.path.exists(mk) == False):
            os.mkdir(mk)
        if (os.path.exists(mk + '/' + ty) == False):
            os.mkdir(mk + '/' + ty)
        if (os.path.exists(mk + '/' + ty + '/' + file_pre) == False):
            os.mkdir(mk + '/' + ty + '/' + file_pre)
        num = i
        # 为了取前三位数字排序
        s = '000000' + str(num)

        file_save = mk + '/' + ty + '/' + file_pre + '/' + \
                    s[-3:] + '-' + '{meta.start:.3f}-{meta.end:.3f}' + '.wav'
        filename = r.save(file_save)
        print("region saved as: {}".format(filename))
    return mk + '/' + ty + '/' + file_pre

# 语音转文本
asr_executor = ASRExecutor()

def audio2txt(path):
    # 返回path下所有文件构成的一个list列表
    print(f"path: {path}")
    filelist = os.listdir(path)
    # 保证读取按照文件的顺序
    filelist.sort(key=lambda x: int(os.path.splitext(x)[0][:3]))
    # 遍历输出每一个文件的名字和类型
    words = []
    for file in filelist:
        print(path + '/' + file)
        text = asr_executor(
            audio_file=path + '/' + file,
            device=paddle.get_device(), force_yes=True) # force_yes参数需要注意
        print(text)
        words.append(text)
    return words


# # 保存
import csv

def txt2csv(txt_all):
    with open('result.csv', 'w', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        for row in txt_all:
            f_csv.writerow([row])
            
if __name__ == "__main__":
    result = qiefen("./long.wav")
    print(result)
    text = audio2txt(result)
    print(text)
    txt2csv(text)