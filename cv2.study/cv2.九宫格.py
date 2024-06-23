import cv2
import numpy as np

def draw_nine_grid(image, points):
    # 确定九宫格的分隔线坐标
    top_left, top_right, bottom_left, bottom_right = points
    middle_top = (top_left + top_right) // 2
    middle_bottom = (bottom_left + bottom_right) // 2
    middle_left = (top_left + bottom_left) // 2
    middle_right = (top_right + bottom_right) // 2
    middle_center = (middle_top + middle_bottom) // 2

    # 绘制九宫格分隔线
    cv2.line(image, tuple(top_left), tuple(top_right), (0, 255, 0), 2)
    cv2.line(image, tuple(top_left), tuple(bottom_left), (0, 255, 0), 2)
    cv2.line(image, tuple(top_right), tuple(bottom_right), (0, 255, 0), 2)
    cv2.line(image, tuple(bottom_left), tuple(bottom_right), (0, 255, 0), 2)
    cv2.line(image, tuple(middle_top), tuple(middle_bottom), (0, 255, 0), 2)
    cv2.line(image, tuple(middle_left), tuple(middle_right), (0, 255, 0), 2)
    cv2.line(image, tuple(top_left), tuple(middle_center), (0, 255, 0), 2)
    cv2.line(image, tuple(middle_top), tuple(middle_center), (0, 255, 0), 2)
    cv2.line(image, tuple(middle_left), tuple(middle_center), (0, 255, 0), 2)

# 示例使用
# 假设矩形的四个顶点坐标为 (x1, y1), (x2, y2), (x3, y3), (x4, y4)
# (x1, y1) 为左上角坐标，(x2, y2) 为右上角坐标，(x3, y3) 为左下角坐标，(x4, y4) 为右下角坐标

# 创建一个空白图像
image = np.zeros((500, 500, 3), dtype=np.uint8)

# 矩形的四个顶点坐标
points = np.array([(100, 100), (400, 100), (400, 400), (100, 400)], dtype=np.int32)

# 在矩形内画出九宫格
draw_nine_grid(image, points)

# 显示图像
cv2.imshow('Nine Grid', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
