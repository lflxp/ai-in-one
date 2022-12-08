# 安装yolov5

- git clone https://github.com/ultralytics/yolov5
- wget https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5s.pt
- cd yolov5 && python detect.py --source data/images/zidane.jpg
- cd yolov5 && python detect.py --source 0 # 摄像头实时物体识别
- android 安装IP摄像头 app
- ios安装idection app

# 调试

- 【基于本地摄像天】python detect.py --source 0
- 【基于自定义阈值】python detect.py --source 0 --hide-conf --conf-thres 0.8
- 【基于实时流推送】python detect.py --source http://admin:admin@192.168.60.100:8081

# 安装face_recognition

- git clone https://github.com/ageitgey/face_recognition

# 参考

- https://blog.csdn.net/m0_58892312/article/details/120923608
- https://howiexue.blog.csdn.net/article/details/118445766?spm=1001.2014.3001.5506
- https://blog.csdn.net/zimiao552147572/article/details/106577644
- https://blog.csdn.net/weixin_43486940/article/details/122559849?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-122559849-blog-106577644.pc_relevant_multi_platform_whitelistv4&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-122559849-blog-106577644.pc_relevant_multi_platform_whitelistv4&utm_relevant_index=1