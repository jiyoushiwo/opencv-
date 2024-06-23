from PIL import Image
import cv2
import numpy as np
import requests

cap=cv2.VideoCapture("Input_Video.MP4")  #初始化摄像头

cascade_src = "cars.xml"
car_cascade = cv2.CascadeClassifier(cascade_src)

# foccs=cv2.VideoWriter_fourcc('M','J','P','G')
# video = cv2.VideoWriter("D:\python_opencv\out.avi",foccs, 15, (640,480))

while (cap.isOpened()): #如果初始化成功
    ret,img=cap.read() #读取视频数据

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, minNeighbors=3,minSize=(80,80))
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        # area = cv2.contourArea(cars)
        print(cars)
    cv2.imshow('img',img)#显示处理后的视频
    c=cv2.waitKey(25)#捕获键盘,25是每一秒播放的速度
    if c==27: #如果时Esc键
       break  #退出
    # video.write(img)
cap.release()   #释放摄像头
cv2.destroyAllWindows()#释放窗口
'''
while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 2)
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
video.write(img)
video.release()
'''
