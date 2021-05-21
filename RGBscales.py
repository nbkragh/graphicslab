
import numpy as np
import sys, os
import cv2
def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    if value < 0:
        lim = 0 - value
        v[v < lim] = 0
        v[v >= lim] -= -1*value
    else:
        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

img1 = cv2.imread(sys.argv[1])
imgREAL = cv2.imread(sys.argv[2])
length = int(sys.argv[3])

imgREAL = rotate_image( imgREAL, 2)

for i in range(length):
	if(imgREAL.shape[1] < img1.shape[1]):
		img1 = cv2.resize(img1, (imgREAL.shape[1],imgREAL.shape[0]), interpolation = cv2.INTER_AREA)
	else:
		imgREAL = cv2.resize(imgREAL, (img1.shape[1],img1.shape[0]), interpolation = cv2.INTER_AREA)


REALRGB = []
avg_color_per_row = np.average(imgREAL, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
print("REAL: "+str(avg_color))
imgREALaverageColor = np.copy(imgREAL)
height, width, depth = imgREALaverageColor.shape
#BLUE
for h in range(0,height):
	for w in range(0,width):
		imgREALaverageColor[h, w] = [avg_color[0],0,0] #color	
REALRGB.append(imgREALaverageColor)
imgREALaverageColor = np.copy(imgREAL)
#GREEN
for h in range(0,height):
	for w in range(0,width):
		imgREALaverageColor[h, w] = [0,avg_color[1],0] #color
REALRGB.append(imgREALaverageColor)
imgREALaverageColor = np.copy(imgREAL)
#RED
for h in range(0,height):
	for w in range(0,width):
		imgREALaverageColor[h, w] = [0,0,avg_color[2]] #color	
REALRGB.append(imgREALaverageColor)

matrixREAL = np.hstack(REALRGB)

img1 = increase_brightness(img1, -40)
cv2.imwrite("brightnesscompensatedVIRTimage.png", img1)
VIRTRGB = []
avg_color_per_row = np.average(img1, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
print("VIRT: "+str(avg_color))
imgVIRTaverageColor = np.copy(img1)
height, width, depth = imgVIRTaverageColor.shape
#BLUE
for h in range(0,height):
	for w in range(0,width):
		imgVIRTaverageColor[h, w] = [avg_color[0],0,0] #color	
VIRTRGB.append(imgVIRTaverageColor)
imgVIRTaverageColor = np.copy(img1)
#GREEN
for h in range(0,height):
	for w in range(0,width):
		imgVIRTaverageColor[h, w] = [0,avg_color[1],0] #color
VIRTRGB.append(imgVIRTaverageColor)
imgVIRTaverageColor = np.copy(img1)
#RED
for h in range(0,height):
	for w in range(0,width):
		imgVIRTaverageColor[h, w] = [0,0,avg_color[2]] #color	
VIRTRGB.append(imgVIRTaverageColor)

matrixVIRT = np.hstack(VIRTRGB)

matrix = np.vstack([matrixVIRT, matrixREAL])
cv2.imwrite("averageColor.png", matrix)
cv2.imshow('image',matrix)
cv2.waitKey(0)