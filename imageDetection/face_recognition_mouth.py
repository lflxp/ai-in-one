# 命令行用法：python detect_open_mouth.py --shape-predictor shape_predictor_68_face_landmarks.dat
 
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
 
"""
mouth_aspect_ratio(mouth)：mouth即给定的口部标志的x/y坐标
	1.A和B分别是计算两组垂直口部标志之间的距离，而C是计算水平口部标志之间的距离。
	  A：51到59的距离。B：53到57的距离。C：49到55的距离。
	  mouth：口部标志的x/y坐标包含了49到68一共19个x/y坐标，索引从0开始，即mouth[0]为49。
	2.计算口部纵横比，然后将口部长宽比返回给调用函数。
		ear = (A + B) / (2.0 * C)
		ear = ((51-59) + (53-57)) / (2.0 * (49-55))
		分子中计算的是口部的特征点在垂直方向上的距离，分母计算的是口部的特征点在水平方向上的距离。
		由于水平点只有一组，而垂直点有两组，所以分母乘上了2，以保证两组特征点的权重相同。
"""
def mouth_aspect_ratio(mouth):
	# 计算两组垂直的坐标之间的欧式距离：计算口中垂直的A(51到59的距离) 和 B(53到57的距离)
	A = dist.euclidean(mouth[2], mouth[10]) # 口中垂直的A(51到59的距离)
	B = dist.euclidean(mouth[4], mouth[8]) # 口中垂直的B(53到57的距离)
	# 计算一组水平的坐标之间的欧式距离：计算口中水平的C(49到55的距离)
	C = dist.euclidean(mouth[0], mouth[6]) #口中水平的C(49到55的距离)
	# 计算嘴长宽比
	mar = (A + B) / (2.0 * C)
	# 返回口长宽比
	return mar
 
# 构造参数解析并解析参数
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=False, default='shape_predictor_68_face_landmarks.dat', help="path to facial landmark predictor")
ap.add_argument("-w", "--webcam", required=False, type=int, default=0, help="index of webcam on system")
args = vars(ap.parse_args())
 
# 定义一个常数，用于表示嘴巴的长宽比
MOUTH_AR_THRESH = 0.79
 
# 初始化dlib的面部检测器（基于HOG），然后创建面部界标预测器
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector() #获取正面人脸检测器
predictor = dlib.shape_predictor(args["shape_predictor"]) #人脸形状预测器：shape_predictor_68_face_landmarks.dat
 
# 抓住嘴巴的坐标索引
(mStart, mEnd) = (49, 68)
 
# 启动视频流线程
print("[INFO] starting video stream thread...")
vs = VideoStream(src=args["webcam"]).start()
time.sleep(1.0)
 
# frame_width = 640
# frame_height = 360
 
# 定义编解码器并创建VideoWriter对象。输出存储在“ outpy.avi”文件中。
# out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))
# time.sleep(1.0)
 
# 循环播放视频流中的帧
while True:
	# 从线程视频文件流中抓取帧，调整其大小，然后将其转换为灰度通道
	frame = vs.read()
	# print(frame.shape)#(480, 640, 3)
	# resize设置width=450时，可以无需同时设置height，因为height会自动根据width所设置的值按照原图的宽高比例进行自适应地缩放调整到合适的值
	frame = imutils.resize(frame, width=640)
	print(frame.shape) #(480, 640, 3)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#转换为单通道的灰度图
 
	# 在灰度框中检测人脸
	rects = detector(gray, 0) #默认值0 即可，表示采样次数
	# 循环每个检测出来的人脸
	for rect in rects:
		# 确定面部区域的面部界标，然后将面部界标（x，y）坐标转换为NumPy数组
		# 传入gray灰度图、还有从灰度图中检测出来的人脸坐标rect
		shape = predictor(gray, rect)
		# 将从灰度图中检测出来的人脸坐标转换为NumPy数组
		shape = face_utils.shape_to_np(shape)
		# 从人脸坐标转换后的NumPy数组中 提取嘴部坐标，然后使用坐标计算嘴部纵横比
		mouth = shape[mStart:mEnd]
 
		# 使用坐标计算嘴部纵横比
		mouthMAR = mouth_aspect_ratio(mouth)
		mar = mouthMAR
		# 计算嘴的凸包，然后可视化嘴
		mouthHull = cv2.convexHull(mouth)
		cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)
		cv2.putText(frame, "MAR: {:.2f}".format(mar), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
 
		# 如果张着嘴 则贴文字
		if mar > MOUTH_AR_THRESH:
			cv2.putText(frame, "Mouth is Open!", (30,60),
			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
 
	# 将图像写入文件“ output.avi”
	# out.write(frame)
	# 显示图像
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# 如果按下“ q”键，则退出循环
	if key == ord("q"):
		break
 
# 做清理
cv2.destroyAllWindows()
vs.stop()