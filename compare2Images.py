
import numpy as np
import sys, os
import cv2


# times = 0
# pixel = 0
# def contrast(c):
# 	global pixel
# 	global times
# 	times = times +1
# 	pixel = pixel + c
# 	return c
# imgfile = sys.argv[1]
# img = Image.open(imgfile)
# img = img.point(contrast)

img1 = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])

print("img1.shape : "+str(img1.shape)+" img2.shape : "+str(img2.shape))
if(img2.shape[1] < img1.shape[1]):
	img1 = cv2.resize(img1, (img2.shape[1],img2.shape[0]), interpolation = cv2.INTER_AREA)
else:
	img2 = cv2.resize(img2, (img1.shape[1],img1.shape[0]), interpolation = cv2.INTER_AREA)


row1 = np.hstack([img1, img2])

avg_color_per_row = np.average(img1, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
print(avg_color)
height, width, depth = img1.shape
for h in range(0,height):
	for w in range(0,width):
		img1[h, w] = avg_color #color
		#img1[:,:,2] += 100 #brightness

avg_color_per_row = np.average(img2, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
print(avg_color)
height, width, depth = img2.shape
for h in range(0,height):
	for w in range(0,width):
		img2[h, w] = avg_color #color
		#img1[:,:,2] += 100 #brightness

row2 = np.hstack([img1, img2])

concatImage = np.vstack([row1, row2])
cv2.imwrite("testerson.png", concatImage)
cv2.imshow('image',concatImage)
cv2.waitKey(0)

