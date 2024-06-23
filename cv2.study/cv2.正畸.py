import os
import cv2
import numpy as np
from tqdm import tqdm


def undistort(frame):
    fx = 685.646752
    cx = 649.107905
    fy = 676.658033
    cy = 338.054431
    k1, k2, p1, p2, k3 = -0.363219, 0.093818, 0.006178, -0.003714, 0.0

    # 相机坐标系到像素坐标系的转换矩阵
    k = np.array([
        [fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]
    ])
    # 畸变系数
    d = np.array([
        k1, k2, p1, p2, k3
    ])
    h, w = frame.shape[:2]
    mapx, mapy = cv2.initUndistortRectifyMap(k, d, None, k, (w, h), 5)
    return cv2.remap(frame, mapx, mapy, cv2.INTER_LINEAR)

# 对摄像头实时视频流做畸变矫正
def distortion_correction_cam():
    cap = cv2.VideoCapture(0)

    # 获取摄像头读取画面的宽和高
    width = cap.get(3)
    height = cap.get(4)
    fps = cap.get(5)
    print(width, height, fps)  # 640.0 480.0 30.0

    # 在这里把摄像头的分辨率修改为和我们标定时使用的一样的分辨率 1280x720
    cap.set(3, 1280)
    cap.set(4, 720)
    width = cap.get(3)
    height = cap.get(4)
    print(width, height, fps)  # 1280.0 720.0 30.0


    while (cap.isOpened()):
        ret, frame = cap.read()
        print(frame.shape)
        undistort_frame = undistort(frame)
        compare = np.hstack((frame, undistort_frame))
        cv2.imshow('frame', compare)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    # input_dir = "/home/shl/extract_rosbag_data/0324_bags/plycal_calib/root/images"
    # output_dir = "/home/shl/extract_rosbag_data/0324_bags/plycal_calib/root/distro_imgs"
    # distortion_correction_imgs(input_dir, output_dir)

    distortion_correction_cam()
