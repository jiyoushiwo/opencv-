import cv2
import numpy as np

img = cv2.imread('greencolor.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gs_frame = cv2.GaussianBlur(imgray, (5,5), 0)
ret, thresh = cv2.threshold(gs_frame, 250, 255, cv2.THRESH_BINARY)
print(ret)
cv2.imshow("thre",thresh)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.imshow('imageshow', img)  # 显示返回值image，其实与输入参数的thresh原图没啥区别
cv2.waitKey(0)

img = cv2.drawContours(img, contours, -1, (255, 0, 0), 2)  # img为三通道才能显示轮廓
#寻找轮廓，轮廓是一系列的点连成的曲线，用来描述物体的基本外形
'''
findContours()函数的三个参数分别表示：输入图像（二值化图像），轮廓检索模式，轮廓近似方法
轮廓的检索模式有四种
1.cv2.RETR_EXTERNAL表示只检测外轮廓，这种方法只寻找最高级的轮廓
2.cv2.RETR_LIST检测的轮廓不建立等级关系
3.cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
4.cv2.RETR_TREE建立一个等级树结构的轮廓。
'''
'''
第三个参数method为轮廓的近似办法
1.cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
2.cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
3.cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法
'''

'''
   findContours()函数的返回值有两个
   1.contours表示轮廓所有像素点的坐标
   2.hieerarchy表示轮廓对应的属性
'''
#轮廓检测是在阀值化的图像上进行的，因为我们是在原始图上进行绘制，所以显示的是彩色结果
cv2.imshow('demo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()