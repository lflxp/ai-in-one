import face_recognition
import cv2
 
#VideoCapture(0) 打开摄像头，参数是视频文件路径则打开视频
video_capture = cv2.VideoCapture(0)
#初始化用于存储面部位置的列表
face_locations = []
 
while True:
    # 抓取视频流中的每一帧
    ret, frame = video_capture.read()
 
    # 将视频帧的大小调整为1/4以加快面部检测处理
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
 
    """
    face_locations(img, number_of_times_to_upsample=1, model='hog') 
        给定一个图像，返回图像中每个人脸的面部特征位置(眼睛、鼻子等) 
        参数： 
            img：一个image（numpy array类型） 
            number_of_times_to_upsample：从images的样本中查找多少次人脸，该参数值越高的话越能发现更小的人脸。 
            model：使用哪种人脸检测模型。
                “hog” 准确率不高，但是在CPUs上运行更快，“cnn” 更准确更深度（且 GPU/CUDA加速，如果有GPU支持的话），默认是“hog” 
            返回值： 一个元组列表，列表中的每个元组包含人脸的位置(top, right, bottom, left)
    """
    # 查找当前视频帧中的所有面部位置和面部位置编码
    face_locations = face_recognition.face_locations(small_frame, model="hog")
 
    # 遍历每个人脸的位置(top, right, bottom, left)
    for top, right, bottom, left in face_locations:
        # 由于我们在中检测到的帧被缩放到1/4大小，因此此处需要对检测出来的人脸位置(top, right, bottom, left)重新放大4倍
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
 
        # 根据放大4倍后还原到原图规模的人脸位置(top, right, bottom, left)到视频原始帧中 进行提取包含人脸的图像区域
        face_image = frame[top:bottom, left:right]
 
        # 使用高斯模糊来模糊面部图像
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)
 
        # 将模糊的人脸区域放回帧图像中
        frame[top:bottom, left:right] = face_image
 
    # 显示结果图像
    cv2.imshow('Video', frame)
 
    # 按键盘上的“q”键退出！
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# 释放摄像头句柄
video_capture.release()
cv2.destroyAllWindows()