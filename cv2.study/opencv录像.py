
import cv2

cap = cv2.VideoCapture(1)  # 使用默认摄像头，如果要从视频文件中录制，将参数改为文件路径
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 定义视频编码器（这里使用XVID）
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # 创建VideoWriter对象，参数分别为输出文件名、编码器、帧率、画面尺寸
while True:
    ret, frame = cap.read()  # 读取一帧图像

    if ret:
        out.write(frame)  # 将帧写入VideoWriter对象

        cv2.imshow('frame', frame)  # 显示当前帧

        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按下'q'键退出录像
            break
    else:
        break
cap.release()  # 释放VideoCapture对象
out.release()  # 释放VideoWriter对象
cv2.destroyAllWindows()  # 销毁所有窗口


