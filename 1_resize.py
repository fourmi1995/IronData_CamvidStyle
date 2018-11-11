from PIL import Image
import os
import glob

OrigRoot = '/home/fourmi/桌面/Data/'
ImgChangedPath = OrigRoot + 'ChangedImgs/'
MaskChangedPath = OrigRoot + 'ChangedMasks/'

width = 480
height = 360

if not os.path.exists(ImgChangedPath):
    os.makedirs(ImgChangedPath)

if not os.path.exists(MaskChangedPath):
    os.makedirs(MaskChangedPath)


def resizeImg(ImgPath):
    for root,dirs,files in os.walk(ImgPath,topdown=False):
        for file in files:
            imgpath = root + '/' + file
            savepath = ImgChangedPath + file[:-4]+'.jpg'
            img = Image.open(imgpath)
            new_img = img.resize((width,height),Image.NEAREST)
            new_img.save(savepath)


def resizeMask(MaskPath):
    for root,dirs,files in os.walk(MaskPath,topdown=False):
        for file in files:
            maskpath = root + '/' + file
            savepath = MaskChangedPath + file
            mask = Image.open(maskpath)
            new_mask = mask.resize((width,height),Image.NEAREST)
            new_mask = new_mask.convert('L')
            new_mask.save(savepath)
            


resizeImg(OrigRoot+'Imgs/')
print("Imgs Resized done!!!")
resizeMask(OrigRoot+'Labels/')
print("Labels Resized done!!!")




