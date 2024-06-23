# 1 导入库
import cv2

# 2 加载视频文件
capture = cv2.VideoCapture("video01.mp4")

# 3 读取视频
ret, frame = capture.read()
while ret:
    # 4 ret 是否读取到了帧，读取到了则为True
    cv2.imshow("video", frame)
    ret, frame = capture.read()

    # 5 若键盘按下q则退出播放
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

# 4 释放资源
capture.release()

# 5 关闭所有窗口
cv2.destroyAllWindows()