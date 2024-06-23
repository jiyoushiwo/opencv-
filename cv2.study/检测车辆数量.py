import cv2
import numpy as np
from cv2 import bgsegm

# 判断是否是车辆的最小矩形
min_w = 150
min_h = 150
# 检测线的高度
line_high = 500
# 统计有效车的数组
cars = []
# 线的偏移量
offset = 12
# 统计数量
carno = 0


# 计算中心点函数
def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


cap = cv2.VideoCapture('Input_Video.mp4')
# 引入去背景函数
bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()

if cap is None:
    print("路径问题")
else:
    while True:
        # 读取视频帧
        ret, frame = cap.read()
        # cv2.putText(frame, str(123), (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 2)
        # print(frame.shape)
        if (ret == True):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 去除背景
            blur = cv2.GaussianBlur(gray, (7, 7), sigmaX=5)
            mask = bgsubmog.apply(blur)
            # 卷积核
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
            # 腐蚀操作-去除背景中较小的噪点
            erode = cv2.erode(mask, kernel, iterations=2)
            # 膨胀操作：还原放大车辆
            dilate = cv2.dilate(erode, kernel2, iterations=1)
            # 闭运算-填补车辆像素空隙
            close1 = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel2)
            # close2 = cv2.morphologyEx(close1,cv2.MORPH_CLOSE,kernel2)
            # 发现轮廓
            cnts, hi = cv2.findContours(close1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # 检测线
            cv2.line(frame, (10,line_high), (1300, line_high), (255, 255, 8), 3)
            # 取出轮廓点绘图
            for (i, c) in enumerate(cnts):
                x, y, w, h = cv2.boundingRect(c)
                # 对车辆的宽高进行判断，验证是否是有效的车辆
                isValid = (w >= min_w) & (h >= min_h)
                if (not isValid):
                    continue
                # 得到有效车辆信息
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # 计算有效车辆的中心点
                cpoint = center(x, y, w, h)
                cars.append(cpoint)
                for (x, y) in cars:
                    if (y > line_high - offset & y < line_high + offset):
                        carno += 1
                        cars.remove((x, y))
                        print(carno)
            cv2.putText(frame, str(carno), (250, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 1)

            cv2.imshow('frame', frame)

            # cv2.imshow('dilate',dilate)
        # cv2.putText(frame, str(123), (150, 200),cv2.FONT_HERSHEY_SIMPLEX,5, (0, 255, 0),1)
        key = cv2.waitKey(10)
        if (key == 27):
            break

# 释放缓存资源
cap.release()
# 释放所有窗口
cv2.destroyAllWindows()

