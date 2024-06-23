from cv2 import cv2
import numpy as np

left_camera_matrix = np.array([[392.9351, 0.1468, 310.0016],
                               [0, 393.6869, 279.4163],
                               [0., 0., 1.]])
left_distortion = np.array([[0.0396, -0.0643, 0.0038, 0.0013, 0.0370]])

right_camera_matrix = np.array([[393.0777, 0.4140, 344.1193],
                                [0, 394.0348, 242.2463],
                                [0, 0, 1.0000]])
right_distortion = np.array([[0.0503, -0.0820, 0.0045, 0.0014, 0.0571]])

R = np.matrix([
    [1.0000, 0.0014, 0.0033],
    [-0.0014, 1.0000, 0.0020],
    [-0.0033, -0.0020, 1.0000],
])

# print(R)

T = np.array([-18.1454, -0.3016, 0.4750])  # 平移关系向量

size = (640, 480)  # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)