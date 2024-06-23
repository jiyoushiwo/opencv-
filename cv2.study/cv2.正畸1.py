import cv2
import numpy as np


def undistort_image(image_path):
    # 读取图像
    image = cv2.imread('sekuai.png')

    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 检测角点
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=4, qualityLevel=0.01, minDistance=10)
    corners = np.int0(corners)

    # 定义目标矩形的四个角点坐标
    width, height = image.shape[1], image.shape[0]
    dst_corners = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

    # 计算透视变换矩阵
    perspective_matrix = cv2.getPerspectiveTransform(corners.astype(np.float32), dst_corners)

    # 应用透视变换
    warped_image = cv2.warpPerspective(image, perspective_matrix, (width, height))

    # 显示原始图像和校正后的图像
    cv2.imshow('Original Image', image)
    cv2.imshow('Warped Image', warped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 使用示例
undistort_image('input_image.jpg')
