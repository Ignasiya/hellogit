import cv2

img = cv2.imread('C:/Users/Василий/Documents/practicecode/GBlearn/OpenCV/test.jpg')
print(img.shape)

#img = cv2.resize(img, (500, 500))

cv2.imshow('Result', img)

cv2.waitKey(0) 