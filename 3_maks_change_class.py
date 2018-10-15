from PIL import Image
import numpy as np
import glob
import os

OrigRoot = '/home/fourmi/桌面/Data/'

MaskPath = 'ChangedMasks'
MaskReal = 'MasksReal'

if not os.path.exists(OrigRoot + MaskReal):
    os.mkdir(OrigRoot + MaskReal)

def pixel_value_to_class(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            maskName = root + '/' + file
            saveName = OrigRoot + MaskReal + '/' + file
            im = np.array(Image.open(maskName))
            w = im.shape[0]
            h = im.shape[1]
            for x in range(w):
                for(y) in range(h):
                    if im[x][y]== 38:
                        im[x][y] = 1
                    elif im[x][y] == 75:
                        im[x][y] = 2
                    elif im[x][y] == 113:
                        im[x][y] = 3
                    else:
                        im[x][y] = 0
            img = Image.fromarray(im.astype('uint8'))
            img.save(saveName)

pixel_value_to_class(OrigRoot + MaskPath)
print("the value of the pixel changed done!!")
