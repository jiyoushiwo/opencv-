import cv2
import numpy as np
def GetArea(img1):
    Mask1 = np.zeros(img1.shape, dtype='uint8')
    Pts_list = [[145, 0], [474, 0], [520, 440], [135, 416]]
    Pts = np.array(Pts_list)
    cv2.fillPoly(Mask1, [Pts], (255, 255, 255))
    return Mask1
ball_color = 'blue'

color_dist = {'red': {'Lower': np.array([0, 60, 60]), 'Upper': np.array([6, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'green': {'Lower': np.array([35, 43, 35]), 'Upper': np.array([90, 255, 255])},
              }
imgPath = r'output.avi'
cap = cv2.VideoCapture(imgPath)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
while True:
    # 获取摄像头图像帧
    cv2.resizeWindow('img', 960, 540)
    cv2.moveWindow('img', 100, 100)
    ret, frame = cap.read()

    # 掩膜遮原图像
    Mask = GetArea(frame)  # 返回的是BGR形式的掩膜黑白图

    grey_Mask = cv2.cvtColor(Mask, cv2.COLOR_BGR2GRAY)  # 灰度图形式的掩膜黑白图
    img_mask = cv2.bitwise_and(frame, frame, mask=grey_Mask)  # 对原图像进行按位与处理，完成掩膜遮盖效果

    # 高斯滤波 + 原图转灰度图
    gs_frame = cv2.GaussianBlur(img_mask, (3, 3), 0)

    hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)  # 转化成HSV图像
    erode_hsv = cv2.erode(hsv, None, iterations=2)
    inRange_hsv = cv2.inRange(erode_hsv, color_dist[ball_color]['Lower'], color_dist[ball_color]['Upper'])
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if cnts:
        c = max(cnts, key=cv2.contourArea)  # 在边界中找出面积最大的区域

        rect = cv2.minAreaRect(c)  # 绘制出该区域的最小外接矩形

        box = cv2.boxPoints(rect)  # 记录该矩形四个点的位置坐标
        cv2.drawContours(frame, [np.int0(box)], -1, (0, 255, 255), 2)  # 绘制矩形轮廓，2是线宽

    grey = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2GRAY)
    erode_hsv = cv2.erode(grey, None, iterations=2)  # 灰度图腐蚀

    # 灰度图转二值图，通过阈值划分获取到正方形木板
    yuzhi, erzhi = cv2.threshold(grey, thresh=125, maxval=255, type=cv2.THRESH_BINARY)
    D_erzhi = cv2.erode(erzhi, None, iterations=6)  # 二值图腐蚀,效果基本可观

    # 得到木板二值图白区矩形的顶点
    cnts, hierarchy = cv2.findContours(D_erzhi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key=cv2.contourArea)
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    print(box)
    point_0 = box[0]  # 左上角的顶点
    point_1 = box[1]  # 右上角的顶点
    point_2 = box[2]  # 右下角的顶点
    point_3 = box[3]  # 左下角的顶点

    # mid_x = (int(box[0][0]) + int(box[3][0])) / 2
    # mid_y = (int(box[0][1]) + int(box[3][1])) / 2
    #
    # third_x = (2 * mid_x + int(box[0][0])) / 3
    # third_y = (2 * mid_y + int(box[3][1])) / 3
    #
    # print(box[0][0])
    #
    # cv2.line(frame,(int(third_x),int(third_x)),(int(box[3][0]),int(box[3][1])),(255,0,0),1)



    # 绘制最小矩形中心点
    M = cv2.moments(box)
    center_x = int(M['m10']/M['m00'])
    center_y = int(M['m01']/M['m00'])
    cv2.circle(frame, (int(center_x), int(center_y)), 1, (0, 0, 255), thickness=4)
    cv2.drawContours(frame, [np.int0(box)], -1, (255, 0, 0), 2)

    cv2.imshow('img', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
cap.release()
cv2.destroyAllWindows()



