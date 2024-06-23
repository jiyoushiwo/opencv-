import cv2
import numpy as np
#定义两个核	（kernel_Ero用于腐蚀，kernel_Dia用于膨胀）
kernel_Ero = np.ones((3,1),np.uint8)
kernel_Dia = np.ones((3,5),np.uint8)

def drawshape(src,points):
    i = 0
    while i < len(points):
        if (i == len(points)-1):
            x,y = points[i][0]
            x1,y1 = points[0][0]
            cv2.line(src,(x,y),(x1,y1),(0, 255, 0), 2)
        else:
            x,y = points[i][0]
            x1,y1 = points[i+1][0]
            cv2.line(src,(x,y),(x1,y1),(0,255,0),1)
        i = i+1

img = cv2.imread("lunzi.jpg")
# cv2.imshow('img',img)
print(img.shape)
# copy_img = img.copy()
#原图copy修改尺寸
# copy_img = cv2.resize(copy_img,(1600,800))
#灰度值转换
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(imgGray.shape)
#高斯滤波去噪
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
#阈值处理
ret,thresh = cv2.threshold(imgBlur,110,255,cv2.THRESH_BINARY)
#腐蚀
imgEro = cv2.erode(thresh,kernel_Ero,iterations=2)
#膨胀
imgDia = cv2.dilate(imgEro,kernel_Dia,iterations=4)

#轮廓检测
# ret,contouts = cv2.findContours(imgDia,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contouts, hierarchy = cv2.findContours(imgDia,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# cnt = contouts
# cv2.drawContours(img,contouts, -1, (0, 255, 0), 3)
# 绘制轮廓
# cv2.drawContours(img,contouts, -1, (0, 255, 0), 3)

# 绘制逼近轮廓
# e = 5
# approx = cv2.approxPolyDP(contouts[2], e, True)
# drawshape(img,approx)
#
# # 绘制凸包
# hull = cv2.convexHull(contouts[2])
# drawshape(img, hull)
print(contouts)

# x, y, w, h = cv2.boundingRect(contouts[1])
# cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#最小外接矩形
# 获取最小外接矩阵，中心点坐标，宽高，旋转角度
for i in contouts:
    rect = cv2.minAreaRect(i)
    x, y, w, h = cv2.boundingRect(i)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
    # 获取矩形四个顶点，浮点型
    box = cv2.boxPoints(rect)
    # 取整
    box = np.int0(box)#将box中的所有元素转换为整数类型
    cv2.drawContours(img,[box],0,(0,0,255),2)

# 显示图像
cv2.imshow('img', img)

# 循环等待按键输入
while True:
    if cv2.waitKey(20) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()


#轮廓逼近
# e = 20
# approx =cv2.approxPolyDP(contouts[0],e,True)
# drawshape(img,approx)
#
# hull = cv2.convexHull(contouts[0])
# drawshape(img,hull)
# print(approx)
# cv2.imshow('ing', img)
# for i in cnt:
#     #坐标赋值
#     x,y,w,h = cv2.boundingRect(i)
#     #roi位置判断
#     if y>20 and y<30 and x<12 and w>50 and h>10:
#         # 画出轮廓
#         cv2.drawContours(copy_img, i, -1, (0, 255, 0), 2)


# while True:
#     # cv2.imshow('bin', binary)
#     # cv2.imshow('ing', img)
#     # cv2.imshow('img', imgGray)
#     # cv2.imwrite('new.jpg',img)
#     if cv2.waitKey(20) & 0xff == ord('q'):#按q退出程序
#         break
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
