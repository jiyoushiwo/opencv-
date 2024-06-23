import cv2
import numpy as np
img = cv2.imread('img.png')#导入图片，路径为相对于工作目录(Python 脚本的运行路径)的路径
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny_img = cv2.Canny(gray,5,50,150)
cv2.imshow('w',canny_img)
def draw_line(img,lines):
    # 绘制直线
    for line_points in lines:
        cv2.line(img,(line_points[0][0],line_points[0][1]),(line_points[0][2],line_points[0][3]),
                 (0,255,0),2,8,0)
    cv2.imshow("line_img", img)
    cv2.waitKey(0)
# #Hough直线检测
lines = cv2.HoughLinesP(canny_img,1,np.pi/180,70,minLineLength=30,maxLineGap=10)
#基于边缘检测的图像来检测直线
draw_line(img,lines)




cv2.imshow('sss', img)#显示图像
cv2.waitKey(0)
cv2.destroyAllWindows()