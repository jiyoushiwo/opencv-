"""
   @Author   : C
   @Time     : 2021/12/29 9:22
   @FileName : GetPoint.py
   @Function :
"""
import cv2


def get_area_points(img):
    count = 1
    a = []
    b = []
    Points = []
    Points_list = []  # 用来放不同的数据

    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # 得到一个字符串
            xy = "%d,%d" % (x, y)
            a.append(x)
            b.append(y)
            # 输出颜色
            print('颜色' + str(img[y, x, 0]) + '   ' + str(img[y, x, 1]) + '   ' + str(img[y, x, 2]))
            # 标记
            cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)  # 绘圆点
            # 标记坐标
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 255), thickness=1)
            # 再次展示图片
            cv2.imshow("{}.jpg".format(count), img)
            # 将点放入列表
            Points.append([a[-1], b[-1]])
            print(a[-1], b[-1])

    while True:
        # 创建窗口
        cv2.namedWindow("{}.jpg".format(count), cv2.WINDOW_NORMAL)
        cv2.resizeWindow("{}.jpg".format(count), 960, 540)
        cv2.moveWindow("{}.jpg".format(count), 100, 100)
        # cv2.setWindowProperty("{}.jpg".format(count), cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # 设置回调函数
        cv2.setMouseCallback("{}.jpg".format(count), on_EVENT_LBUTTONDOWN)
        # 展示图片
        cv2.imshow("{}.jpg".format(count), img)
        # 等待按键，按下空格键表示标记完成一个区域，按下enter键表示所有区域标记完成
        flag = cv2.waitKey()
        # 空格键表示下一个区域
        if flag == 32:
            if Points:  # 列表不为空
                Points_list.append(Points)
            Points = []
        # Enter键表示结束
        if flag == 13:
            if Points:
                Points_list.append(Points)
            break
    return Points_list


if __name__ == '__main__':
    path ="chedao.jpg"

    img = cv2.imread(path)
    Pts_list = get_area_points(img)

    print('o.o')

    # FileName = r"D:\cycFeng\Data\20211220\Yuce\Point.txt"  # Point.txt
    # if os.path.exists(FileName):  # 如果文件存在
    #     os.remove(FileName)
    # file = open(FileName, 'w')  # 新建文件



