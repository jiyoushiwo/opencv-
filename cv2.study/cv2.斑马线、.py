import cv2
import numpy as np

#读取图片
img = cv2.imread('zippa_line.jpg')
print(img.shape)
#灰度化，将图片转为单通道
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#print(gray.shape)
#二值化cv2.threshold(src, thresh, maxval, type[, dst])
# src：表示的是图片源
# thresh：表示的是阈值（起始值）
# maxval：表示的是最大值
# type：表示的是这里划分的时候使用的是什么类型的算法，常用值为0（cv2.THRESH_BINARY）
ret,binary = cv2.threshold(gray,150,240,0)

#轮廓查找
contours, hierarchy =cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1,(0,255,255),3)
print(contours)

# cv2.imshow('bin',binary)
# cv2.imshow('ing',img)
# cv2.imshow('img',gray)
while True:
    cv2.imshow('bin', binary)
    cv2.imshow('ing', img)
    cv2.imshow('img', gray)
    if cv2.waitKey(20) & 0xff == ord('q'):#按q退出程序
        break
        cv2.waitKey(0)