import cv2
img=cv2.imread("all.jpg")
# 读取原始图像
templ = cv2.imread("lunzi.jpg")
templ = cv2.resize(templ,(200,200))
height,width,c = templ.shape
results = cv2.matchTemplate(img,templ,cv2.TM_CCOEFF_NORMED)
#获取匹配结果的最小值、最大值、最小值坐标、最大值坐标
minValue,maxValue,minLoc,maxLoc = cv2.minMaxLoc(results)
resultPoint1 = maxLoc
resultPoint2 = (resultPoint1[0]+width,resultPoint1[1]+height)
cv2.rectangle(img, resultPoint1,resultPoint2, (0,0,255),2)
cv2.imshow("img", img)
cv2.imshow("img1", templ)
        # 显示匹配的结果
cv2.waitKey(0)
cv2.destroyAllWindows()