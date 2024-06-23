'''opencv检测人脸，双眼，嘴'''

import cv2
detector=cv2.CascadeClassifier(r'D:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r"D:\Python\Lib\site-packages\cv2\data\haarcascade_eye_tree_eyeglasses.xml")
mouth = cv2.CascadeClassifier(r"D:\Python\Lib\site-packages\cv2\data\haarcascade_smile.xml")
cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray,minSize=(100,100),flags=cv2.CASCADE_SCALE_IMAGE)

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        # cv2.imshow('roi_gray',roi_gray)
        cv2.imshow('roi_color', roi_color)
        cv2.putText(img, 'dog_face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)
        eyes = eye_cascade.detectMultiScale(roi_gray, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        mouths = mouth.detectMultiScale(roi_gray, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            cv2.putText(img,'eye',(ex,ey-1),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,255),2)
        for (mx,my,mw,mh) in mouths:
            cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (0, 255, 0), 2)

            cv2.putText(img, 'mouth', (mx+100, my+100), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv2.imshow('frame', img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
