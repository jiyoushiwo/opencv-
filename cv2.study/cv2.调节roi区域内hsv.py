import cv2
import numpy as np

def empty(a):
    pass

def set_roi(event, x, y, flags, param):
    global roi_top_left, roi_bottom_right, roi_selected, roi_selection_started
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_top_left = (x, y)
        roi_selection_started = True
        roi_selected = False
    elif event == cv2.EVENT_LBUTTONUP:
        roi_bottom_right = (x, y)
        roi_selected = True
        roi_selection_started = False

# 初始化全局变量
roi_top_left = (100, 100)
roi_bottom_right = (300, 300)
roi_selected = False
roi_selection_started = False

# 创建Trackbar窗口
cv2.namedWindow("ROI")
cv2.setMouseCallback("ROI", set_roi)
cv2.resizeWindow("ROI", 640, 480)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    # 在图像上绘制ROI区域选择
    if roi_selection_started and not roi_selected:
        temp_img = img.copy()
        cv2.rectangle(temp_img, roi_top_left, (roi_top_left[0] + 1, roi_top_left[1] + 1), (0, 255, 0), 2)
        cv2.imshow("ROI", temp_img)

    # 获取ROI区域
    roi_x, roi_y = roi_top_left
    roi_width = roi_bottom_right[0] - roi_top_left[0]
    roi_height = roi_bottom_right[1] - roi_top_left[1]
    roi = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]

    # 转换为HSV颜色空间
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # 创建颜色调节滑动条
    cv2.createTrackbar("Hue Min", "ROI", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "ROI", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "ROI", 0, 255, empty)
    cv2.createTrackbar("Sat Max", "ROI", 255, 255, empty)
    cv2.createTrackbar("Val Min", "ROI", 0, 255, empty)
    cv2.createTrackbar("Val Max", "ROI", 255, 255, empty)

    # 读取HSV滑块值
    h_min = cv2.getTrackbarPos("Hue Min", "ROI")
    h_max = cv2.getTrackbarPos("Hue Max", "ROI")
    s_min = cv2.getTrackbarPos("Sat Min", "ROI")
    s_max = cv2.getTrackbarPos("Sat Max", "ROI")
    v_min = cv2.getTrackbarPos("Val Min", "ROI")
    v_max = cv2.getTrackbarPos("Val Max", "ROI")

    # 设定HSV阈值范围
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # 根据阈值进行图像分割，提取ROI区域内的特定颜色
    mask = cv2.inRange(hsv_roi, lower, upper)
    imgResult = cv2.bitwise_and(roi, roi, mask=mask)

    # 在原始帧上绘制ROI区域
    cv2.rectangle(img, roi_top_left, roi_bottom_right, (0, 255, 0), 2)

    # 在原始帧上显示ROI区域内的颜色分割结果
    img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width] = imgResult

    # 展示图像
    cv2.imshow("Image", img)

    # 按下任意键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
