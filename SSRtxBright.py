
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

folder = sys.argv[1]
filebasename = sys.argv[2]
imgREAL = cv2.imread(sys.argv[3])
roughness = int(sys.argv[4])
length = int(sys.argv[5])

imgREAL = rotate_image( imgREAL, 2)
imgREAL = cv2.cvtColor(imgREAL, cv2.COLOR_BGR2GRAY)
img1 = cv2.imread(folder+"/"+filebasename+"_SS1to10-"+str(1)+"_R1to10-"+str(1)+".png")


print("img1.shape : "+str(img1.shape)+" imgREAL.shape : "+str(imgREAL.shape))



rows = []
for j in range(length):
    img = []
    for i in range(length):
        img1 = cv2.imread(folder+"/"+filebasename+"_SS1to10-"+str(i+1)+"_R1to10-"+str(roughness)+".png")
        if(imgREAL.shape[1] < img1.shape[1]):
            img1 = cv2.resize(img1, (imgREAL.shape[1],imgREAL.shape[0]), interpolation = cv2.INTER_AREA)
        else:
            imgREAL = cv2.resize(imgREAL, (img1.shape[1],img1.shape[0]), interpolation = cv2.INTER_AREA)
        img1 = increase_brightness(img1, -10*j)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img.append(img1)
        img.append(imgREAL)
    rows.append(np.hstack(img))

matrix = np.vstack(rows)
#concatImage = np.vstack([row1, imgREAL])
cv2.imwrite("testerson.png", matrix)
cv2.imshow('image', matrix)
cv2.waitKey(0)




