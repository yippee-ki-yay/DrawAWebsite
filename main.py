import cv2

img = cv2.imread('test_img1.jpg')

greyimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(greyimg,60,255, 0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 2)

cv2.imwrite('out.jpg', img)
