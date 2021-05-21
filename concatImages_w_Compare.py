from PIL import Image
import numpy as np
import sys, os

folder = sys.argv[1]
filebasename = sys.argv[2]
length = int(sys.argv[3])

imgREAL = Image.open("klodsREAL_highlight.png")
imgREAL = imgREAL.rotate(2)
imgREAL = imgREAL.resize((imgREAL.size[0],imgREAL.size[1]), Image.ANTIALIAS)
for file in os.listdir(folder):
    if file.endswith(".png"):
        img = Image.open(folder+"/"+str(file))
        print(imgREAL.size)
        break

print(length*int(imgREAL.size[0]))        
concatImage = Image.new('RGB', (length*int(imgREAL.size[0]),length*int(imgREAL.size[1]/2)), (250,250,250) )
for i in range(int(length/2)):
    for j in range(int(length/2)):
        filename = filebasename+"_SS1to10-"+str(i+1)+"_R1to10-"+str((j+1))+".png"
        print(filename)
        currentImage = Image.open(folder+"/"+filename)
        currentImage = currentImage.rotate(6)
        currentImage = currentImage.resize((imgREAL.size[0],imgREAL.size[1]), Image.ANTIALIAS)
        concatImage.paste(currentImage, (imgREAL.size[0]*(j*2),imgREAL.size[1]*(i)))
        concatImage.paste(imgREAL, (imgREAL.size[0]*(j*2+1),imgREAL.size[1]*(i)))
concatImage.save(filebasename+"_w_Compare.png", "PNG")
concatImage.show()