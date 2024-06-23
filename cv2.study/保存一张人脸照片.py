import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame = cap.read()
    # frame = cv2.flip(frame,0)
    cv2.imshow('shot',frame)
    k = cv2.waitKey(5)
    if k == ord('s'):
       cv2.imwrite('myface.jpg',frame)
    if k == 27:
        break