import cv2
import numpy as np
from PIL import Image
blur_ksice = 5
canny_lth = 50
canny_hth = 150

#对图像进行处理
img = cv2.imread('chedao.jpg')
print(img.shape)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
blur_gray = cv2.GaussianBlur(gray,(blur_ksice,blur_ksice),1)
edges = cv2.Canny(blur_gray,canny_lth,canny_hth)



def roi_mask(img,corner_points):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask,corner_points,255)
    masked_img = cv2.bitwise_and(img,mask)
    return masked_img

#标记四个点用于roi截取
rows,cols = edges.shape#返回值为图像的像素行列
points = np.array([[(122,447),(348,293),(483,286),(731,450)]])
# print(points)
roi_edges = roi_mask(edges,points)
cv2.imshow('roi',roi_edges)

'''霍夫变换，找出直线'''
lines = cv2.HoughLinesP(edges,1,np.pi/180,15,40,200)
# x1,y1,x2,y2 =
def calculate_slope(line):
    x1,y1,x2,y2=line[0]
    return (y2-y1)/(x2-x1)
def draw_line(img,lines):
    # 绘制直线
    for line_points in lines:
        if calculate_slope(line_points) == 0:
            pass
        cv2.line(img,(line_points[0][0],line_points[0][1]),(line_points[0][2],line_points[0][3]),
                 (0,255,0),2,8,0)
    cv2.imshow("line_img", img)
    cv2.waitKey(0)
# #Hough直线检测
lines = cv2.HoughLinesP(roi_edges,1,np.pi/180,70,minLineLength=5,maxLineGap=10)
#基于边缘检测的图像来检测直线
draw_line(img,lines)

def calculate_slope(line):
    x1,y1,x2,y2=line[0]
    k = (y2 - y1) / (x2 - x1)
    print('%0.2f'%k)
    return (y2-y1)/(x2-x1)
# for i in lines:
#     x1, y1, x2, y2 = lines[0]
left_lines = [line for line in lines if calculate_slope(line)>0]
right_lines = [line for line in lines if calculate_slope(line)<0]
print(left_lines)
'''离群值过滤'''
def reject_abnormal_lines(lines,threshold):
    slopes = [calculate_slope(line) for line in lines]
    while len(lines)>0:
        mean = np.mean(slopes)
        diff = [abs(s-mean) for s in slopes]#取斜率的绝对值
        idx = np.argmax(diff)#取数组中每一行或每一列的最大值
        if diff[idx] > threshold:
            slopes.pop(idx)
            lines.pop(idx)
        else:
            break
    return lines
reject_abnormal_lines(left_lines,threshold=0.2)
reject_abnormal_lines(right_lines,threshold=0.2)

"""最小二乘拟合"""
def least_squares_fit(lines):
    x_coords = np.ravel([[line[0][0],line[0][2]]] for line in lines)
    y_cords =  np.ravel([[line[0][1],line[0][3]]] for line in lines)
    poly = np.polyfit(x_coords,y_cords)
    print(poly)
    point_min = (np.min(x_coords),np.polyval(poly,np.min(x_coords)))
    point_max = (np.max(x_coords),np.polyval(poly,np.max(x_coords)))
    return np.array([point_min,point_max],dtype=np.int)
cv2.line(img,left_lines[0],left_lines[1],color=(0,255,0),thickness=2)
cv2.line(img,right_lines[0],right_lines[1],color=(0,255,0),thickness=2)



cv2.imshow('che',edges)
cv2.imshow('roi',roi_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()


#

