#1.canny边缘检测  2.mask   3.霍夫变换   4.离群值过滤    5.最小二乘拟合     6.绘制直线

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''1.canny边缘检测'''
img=cv2.imread('chedao2.jpg',cv2.IMREAD_GRAYSCALE)     #以灰度图形式读取图片，为canny边缘检测做准备
img0=cv2.imread("chedao2.jpg",cv2.IMREAD_COLOR)

edge_img=cv2.Canny(img,200,300)     #设定阈值，低于阈值被忽略，高于阈值被显示，
                                       # 阈值的设定与图片的色彩有关，需要手动调整到合适的值（使车道线清晰显示出来）

# plt.imshow(img)
# plt.show()
# #
# cv2.namedWindow('edge_img',0)
# cv2.resizeWindow('edge_img',500,800)
# cv2.imshow('edge_img',edge_img)
# cv2.waitKey(0)

'''2.roi_mask(提取感兴趣的区域)'''
mask=np.zeros_like(edge_img)   #变换为numpy格式的图片
mask=cv2.fillPoly(mask,np.array([[[0,460],[1150,470],[780,0],[650,0]]]),color=255)   #对感兴趣区域制作掩膜
#在此做出说明，实际上，车载相机固定于一个位置，所以对于感兴趣的区域的位置也相对固定，这个视相机位置而定。
cv2.namedWindow('mask',0)
cv2.resizeWindow('mask',800,1200)
cv2.imshow('mask',mask)
cv2.waitKey(0)
masked_edge_img=cv2.bitwise_and(edge_img,mask)   #与运算
# cv2.namedWindow('masked_edge_img',0)
# cv2.resizeWindow('masked_edge_img',800,1200)
# cv2.imshow('masked_edge_img',masked_edge_img)
# cv2.waitKey(0)


'''3.霍夫变换，找出直线'''
def calculate_slope(line):
    '''计算线段line的斜率
    ：param Line：np.array([[x_1,y_1,x_2,y_2]])
    :return:
    '''
    x_1,y_1,x_2,y_2=line[0]
    return (y_2-y_1)/(x_2-x_1)


lines=cv2.HoughLinesP(masked_edge_img,1,np.pi/180,15,minLineLength=50,maxLineGap=20)    #获取所有线段

left_lines=[line for line in lines if calculate_slope(line)>0]
right_lines=[line for line in lines if calculate_slope(line)<0]


'''4.离群值过滤'''

def reject_abnormal_lines(lines,threshold):
    '''剔出斜率不一致的线段'''
    slopes=[calculate_slope(line) for line in lines]
    while len(lines)>0:
        mean=np.mean(slopes)
        diff=[abs(s-mean) for s in slopes]
        idx=np.argmax(diff)
        if diff[idx]>threshold:
            slopes.pop(idx)
            lines.pop(idx)
        else:
            break
    return lines
print(len(left_lines),len(right_lines))

reject_abnormal_lines(left_lines,threshold=0.1)
reject_abnormal_lines(right_lines,threshold=0.1)
print(len(left_lines),len(right_lines))


'''5.最小二乘拟合 把识别到的多条线段拟合成一条直线'''
  #np.ravel: 将高维数组拉成一维数组
# np.polyfit:多项式拟合
#np.polyval: 多项式求值

def least_squares_fit(lines):

    x_coords=np.ravel([[line[0][0],line[0][2]] for line in lines])
    y_coords = np.ravel([[line[0][1], line[0][3]] for line in lines])   #取出所有标点
    poly=np.polyfit(x_coords,y_coords,deg=1)                             #进行直线拟合，得到多项式系数
    point_min=(np.min(x_coords),np.polyval(poly,np.min(x_coords)))
    point_max = (np.max(x_coords), np.polyval(poly, np.max(x_coords)))     #根据多项式系数，计算两个直线上的点
    return np.array([point_min,point_max],dtype=np.int64)

left_lines=least_squares_fit(left_lines)
right_lines=least_squares_fit(right_lines)

'''6.直线绘制'''
cv2.line(img0,tuple(left_lines[0]),tuple(left_lines[1]),color=(0,255,255),thickness=5)
cv2.line(img0,tuple(right_lines[0]),tuple(right_lines[1]),color=(0,255,255),thickness=5)

cv2.namedWindow('lane',0)
cv2.resizeWindow('lane',800,1200)
cv2.imshow('lane',img0)
cv2.waitKey(0)


