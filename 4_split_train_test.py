import os
import random
from PIL import Image
import numpy as np
import glob 

OrigRoot = '/home/fourmi/桌面/Data/'
imgs_all = 'ChangedImgs/'
mask_all = 'MasksReal/'

TrainSplitRoot = '/home/fourmi/桌面/IronData_Camvid/training/'
train_imgs =  TrainSplitRoot + 'imgs/'
train_masks = TrainSplitRoot + 'labels/'

TestSplitRoot = '/home/fourmi/桌面/IronData_Camvid/testing/'
test_imgs =  TestSplitRoot + 'imgs/'
test_masks = TestSplitRoot + 'labels/'

if not os.path.exists(train_imgs):
    os.makedirs(train_imgs)

if not os.path.exists(train_masks):
        os.makedirs(train_masks)

if not os.path.exists(test_imgs):
        os.makedirs(test_imgs)

if not os.path.exists(test_masks):
        os.makedirs(test_masks)


def split_train_test(path,scale):
    Names = []
    Indexs = []
    for root, dirs, files in os.walk(path):
        for file in files:
            Names.append(file)
    for index in range(len(Names)):
        Indexs.append(index)
    random.shuffle(Indexs)
    number = 0
    for number in range(len(Indexs)):
        if number < (int) (scale * len(Indexs)):
            ImgName = OrigRoot + imgs_all + Names[Indexs[number]]
            TrainImgName = train_imgs + Names[Indexs[number]]
            MaskName = OrigRoot + mask_all + Names[Indexs[number]][:-4]+'.png'
            TrainMaskName = train_masks + Names[Indexs[number]][:-4]+'.png'
            img = Image.open(ImgName)
            mask = Image.open(MaskName)
            img.save(TrainImgName)
            mask.save(TrainMaskName)
            #print(ImgName)
            #print(TrainImgName)
            #print(MaskName)
            #print(TrainMaskName)
        else:
            ImgName = OrigRoot + imgs_all + Names[Indexs[number]]
            TestImgName = test_imgs + Names[Indexs[number]]
            MaskName = OrigRoot + mask_all + Names[Indexs[number]][:-4]+'.png'
            TestMaskName = test_masks + Names[Indexs[number]][:-4]+'.png' 
            img = Image.open(ImgName)
            mask = Image.open(MaskName)
            img.save(TestImgName)
            mask.save(TestMaskName)

split_train_test(OrigRoot + imgs_all, 0.8)
print("splited done!!!")            
