import sensor, image, time, pyb
# import car
from pyb import Servo
import time

s1 = Servo(1)  # 对应p7引脚
s2 = Servo(2)  # 对应p8引脚
# You may need to tweak the above settings for tracking green things...
# Select an area in the Framebuffer to copy the color settings.

sensor.reset()  # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565)  # use RGB565.
sensor.set_framesize(sensor.QQVGA)  # use QQVGA for speed.
sensor.skip_frames(10)  # Let new settings take affect.
sensor.set_auto_whitebal(False)  # turn this off.
clock = time.clock()  # Tracks FPS.
led = pyb.LED(3)
uart = pyb.UART(3, 115200, timeout_char=1000)  # 定义串口3变量timeout_char是超时时间，超时1秒跳出
led.on()

h3 = 0
x3 = 0
green_threshold = (67, 100, -128, 127, 26, 127)
size_threshold = 2000


def find_max(blobs):  # 寻找最大的小球
    max_size = 0
    for blob in blobs:
        if blob[2] * blob[3] > max_size:
            max_blob = blob
            max_size = blob[2] * blob[3]
    return max_blob


def pidx(a):  # x方向上的pid控制
    global x3
    kpx = 0.2
    kix = 0.02
    x2 = a - 0
    x3 += x2
    x4 = x2 * kpx + x3 * kix
    if x4 > 80:
        x4 = 80
    if x4 < -80:
        x4 = -80
    return x4


def pidh(b):  # h方向上的pid控制
    global h3
    kph = 0.3
    kih = 0.02
    h2 = b - 0
    h3 += h2
    h4 = h2 * kph + kih * h3
    if h4 > 80:
        h4 = 80
    if h4 < -80:
        h4 = -60
    return h4


while (True):
    clock.tick()  # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot()  # Take a picture and return the image.

    blobs = img.find_blobs([green_threshold])
    if blobs:
        max_blob = find_max(blobs)
        x = -max_blob[5] + 80  # x轴的坐标
        h_error = max_blob[6]
        h = h_error - 60
        img.draw_rectangle(max_blob[0:4])  # rect
        img.draw_cross(max_blob[5], max_blob[6])  # cx, c
        x1 = pidx(x)
        h1 = pidh(h)
        print(h)
        print("h error: ", h1)
        s1.angle(h1)  # move to 45 degrees
        s2.angle(x1)