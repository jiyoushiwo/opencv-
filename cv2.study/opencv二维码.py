import cv2
from pyzbar import pyzbar

def scan_qr_code(image):
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 创建ZBar图像对象
    zbar_image = pyzbar.Image(gray.shape[1], gray.shape[0], 'Y800', gray.tobytes())

    # 创建ZBar扫描器对象
    scanner = pyzbar.Scanner()

    # 扫描图像中的QR码
    results = scanner.scan(zbar_image)

    # 在图像中标记QR码及其内容
    for result in results:
        # 提取QR码的边界框坐标
        x, y, w, h = result.rect

        # 在图像上绘制边界框
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 提取QR码的内容
        qr_code_data = result.data.decode("utf-8")

        # 在图像上显示QR码的内容
        cv2.putText(image, qr_code_data, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # 读取一帧图像

    if ret:
        # 扫描图像中的QR码
        frame = scan_qr_code(frame)

        # 显示图像
        cv2.imshow('QR Code Scanner', frame)

        # 按下'q'键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 释放资源和销毁窗口
cap.release()
cv2.destroyAllWindows()
