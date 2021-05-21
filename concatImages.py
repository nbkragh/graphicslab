from PIL import Image
import numpy as np
import sys, os
folder = sys.argv[1]
filebasename = sys.argv[2]
length = int(sys.argv[3])

for file in os.listdir(folder):
    if file.endswith(".png"):
        img = Image.open(folder +"/"+str(file))
        print(img.size)
        break

print(length*int(img.size[0]))        
concatImage = Image.new('RGB', (length*int(img.size[0]),length*int(img.size[1])), (250,250,250) )
for i in range(length):
    for j in range(length):
        currentImage = Image.open(folder+"/"+filebasename+"_SS1to10-"+str(i+1)+"_R1to10-"+str((j+1))+".png")
        currentImage = currentImage.rotate(3)
        concatImage.paste(currentImage, (currentImage.size[0]*j,currentImage.size[1]*i))
concatImage.save(filebasename+"_SS_R_table.png", "PNG")
concatImage.show()