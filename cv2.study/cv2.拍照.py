import cv2
import time
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    cv2.imshow("Camera", frame)

    # 等待按键
    key = cv2.waitKey(1)
    if key != -1:
        # 生成文件名，使用当前时间戳作为文件名
        filename = "photo_{}.png".format(int(time.time()))
        # 保存图像到文件
        cv2.imwrite(filename, frame)
        print("Photo saved as", filename)
        break

cap.release()
cv2.destroyAllWindows()
