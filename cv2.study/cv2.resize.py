import cv2
img = cv2.imread('shou.jpg')
cv2.imshow('img',img)
resize = cv2.resize(img,(700,500))
cv2.imshow('resize',resize)
cv2.imwrite("shou1.jpg",resize)

cv2.waitKey(0)
cv2.destroyAllWindows()