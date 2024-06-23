import cv2
import numpy as np
from yanmo import get_area_points


def GetArea(img1):
    # 创建掩膜
    Mask1 = np.zeros(img1.shape, dtype='uint8')
    # 找到顶点列表
    Pts_list = get_area_points(img1)
    # 填充
    for Pts in Pts_list:
        Pts = np.array(Pts)
        cv2.fillPoly(Mask1, [Pts], (255, 255, 255))
    # 返回掩膜
    return Mask1


if __name__ == '__main__':
    # 输入图片地址和保存图片地址
    imgPath = r'photo.jpg'
    # imgPath = r'output.avi'
    # SavePath = r"D:\ma_mask.jpg"
    # 是否保存
    isSave = False

    # 读取图片，得到掩膜
    cap = cv2.VideoCapture(imgPath)#视频掩膜，
    ret, frame = cap.read()
    # img = cv2.imread(imgPath)
    Mask = GetArea(frame)

    # 展示
    cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('mask', 960, 540)
    cv2.moveWindow('mask', 100, 100)
    cv2.imshow('mask', Mask)
    cv2.waitKey()

    # 是否保存
    # if isSave:
    #     cv2.imwrite(SavePath, Mask)
    # 掩膜变成灰度图
    Mask = cv2.cvtColor(Mask, cv2.COLOR_RGB2GRAY)

    img_mask = cv2.bitwise_and(frame, frame, mask=Mask)
    cv2.namedWindow('img_mask', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('img_mask', 960, 540)
    cv2.moveWindow('img_mask', 100, 100)
    cv2.imshow('img_mask', img_mask)
    cv2.waitKey()



