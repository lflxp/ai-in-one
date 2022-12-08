# 简介

针对程序员的ai-in-one程序，提供所见即所得的语音识别、目标检测和人脸识别技术，基于百度pp飞桨实现。

# 目录介绍

## paddlespeech

语音识别相关代码，包括：

* 程序启动
* python依赖安装
* macos以及window兼容性解决
* 语音识别
* 语音切分
* kws自动唤醒

## 

[语音识别文档](./paddlespeech/README.md)

## 目标检测和人脸识别

使用了两个相关开源产品：

* [face_recognition](https://github.com/ageitgey/face_recognition)
* [yolov5](https://github.com/ultralytics/yolov5)
* [paddleDetection](https://github.com/PaddlePaddle/PaddleDetection) (未完待续)

分别实现了：

* [离线人脸识别](./imageDetection/face_recognition/README.md)
* [人脸检测并打马赛克](./imageDetection/yolov5/README.md)
* [本机摄像头目标识别](./imageDetection/yolov5/README.md)
* [图片目标识别](./imageDetection/yolov5/README.md)
* [视频目标识别](./imageDetection/yolov5/README.md)
* [App网络摄像头目标识别](./imageDetection/yolov5/README.md)

## 其它语言支持

还调研了`Go`语言的图形识别技术和测试

- [gocv](./imageDetection/gocv-test/README.md)
- [go-face](./imageDetection/go-face-test/README.md)