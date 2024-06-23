import cv2
import numpy as np
photo = list()
lables = list()
photo.append(cv2.imread('Summer1.jpg',0))
lables.append(0)
photo.append(cv2.imread('Summer2.jpg',0))
lables.append(0)
photo.append(cv2.imread('Summer3.jpg',0))
lables.append(0)

photo.append(cv2.imread('Elvis1.jpg',0))
lables.append(1)
photo.append(cv2.imread('Elvis2.jpg',0))
lables.append(1)
photo.append(cv2.imread('Elvis3.jpg',0))
lables.append(1)

names = {'0':'summer','1':'elvis'}
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.train(photo,np.array(lables))

i = cv2.imread('daice.jpg',0)
lables,confience = recognizer.predict(i)
print('confidence='+str(confience))
print(names[str(lables)])