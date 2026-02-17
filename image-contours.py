#code taken from my other project
import cv2

imgPath = "/home/pi/rc project/rects.png"

tempImg2 = cv2.imread(imgPath,cv2.IMREAD_COLOR)

tempImg = cv2.imread(imgPath,cv2.IMREAD_GRAYSCALE)

print(tempImg2 is None)

cv2.imshow('Contour Chart', tempImg2)

# _, threshold = cv2.threshold(tempImg, 200, 255, cv2.THRESH_BINARY)

# _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# #js use first and most contouring contour for the pixel

# contl = max(contours, key=cv2.contourArea)

# approx = cv2.approxPolyDP(contl, 0.009*cv2.arcLength(contl, True), True)

# cv2.drawContours(tempImg2, [approx], 0, (0,0,255),1)

# cv2.imshow('Contour Chart',tempImg2)

