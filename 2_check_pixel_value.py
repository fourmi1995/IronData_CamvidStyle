from PIL import Image
import numpy as np
import glob
import os

OrigRoot = '/home/fourmi/桌面/Data/'

#MaskPath = 'ChangedMasks'
MaskPath = 'MasksReal'
def check_pixel_value(path):
    for root ,dirs, files in os.walk(path,topdown=False):
        for file in files:
            maskName = root + '/' + file
            im = np.array(Image.open(maskName))
            w = im.shape[0]
            h = im.shape[1]
            for x in range(w):
                for y in range(h):
                    #if(im[x][y]!=0 and im[x][y] != 38 and im[x][y]!=113 and im[x][y]!=75):
                    if(im[x][y]!=1 and im[x][y]!=2 and im[x][y]!=3 and im[x][y]!=0):
                        print(im[x][y])

check_pixel_value(OrigRoot+MaskPath)            
print("checked done!!")
