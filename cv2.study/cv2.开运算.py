import numpy as np
import cv2 as  cv
import matplotlib.pyplot as plt
#1读取图像
img1 = cv.imread("img_1.png")
img2 = cv.imread("img_1.png")
#2创建核结构
kernel = np.ones((10, 10), np.uint8)
'''
    开运算是先腐蚀后膨胀，其作用是：分离物体，消除小区域。特点：消除噪点，去除小的干扰块，而不影响原来的图像。消除白点
    闭运算与开运算相反，冠先膨胀后腐蚀，作用是消除／“闭合”物体里面的孔洞，特点：可以填充闭合区域。消除黑色小块，填补黑洞
    '''
#3图像的开闭运算
cv0pen = cv.morphologyEx(img1, cv.MORPH_OPEN, kernel)#开运算
cvClose = cv.morphologyEx(img2, cv.MORPH_CLOSE, kernel)#闭运算12#4图像展示
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].imshow(img1)
axes[0, 0].set_title("原图")
axes[0, 1].imshow(cv0pen)
axes[0, 1].set_title("开运算结果")
axes[1, 0].imshow(img2)
axes[1, 0].set_title("原图")
axes[1, 1].imshow(cvClose)
axes[1, 1].set_title("闭运算结果")
plt.show()
