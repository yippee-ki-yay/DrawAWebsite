import cv2
import numpy as np

from generate_html import GenerateHtml

input_img = cv2.imread('test_images/layout.jpg')

height, width, ch = input_img.shape

print height, width

generate = GenerateHtml()

grey_img = cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(grey_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,2)

#image transformation dialate/erode
kernel = np.ones((2, 2), np.uint8)
kernel2 = np.ones((3, 3), np.uint8)
kernel3 = np.ones((1, 1), np.uint8)

no_dots = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

morphed_img = cv2.dilate(no_dots, kernel2, iterations = 1)

contours, hierarchy = cv2.findContours(morphed_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

rectangleContours = []

for c in zip(contours, hierarchy[0]):

    curr_countour = c[0]
    curr_hierarchy = c[1]

    x,y,w,h = cv2.boundingRect(curr_countour)
    area = cv2.contourArea(curr_countour, True)

    if curr_countour.size > 100 and area < 0:
        print curr_hierarchy, w, h,x, y
        rectangleContours.append(curr_countour)


cv2.drawContours(input_img, rectangleContours, -1, (0,255,0), 2)

#process contours and create divs
generate.process_divs(input_img, rectangleContours)

generate.write_html("first")

cv2.imwrite('out.jpg', input_img)
