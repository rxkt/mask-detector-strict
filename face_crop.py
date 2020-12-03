import numpy as np
import cv2
import os
import os.path
import shutil
import sys

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

types = ['Mask', 'Non Mask']
sets = ['Test', 'Train', 'Validation']
baseDir = './data/New Masks Dataset/'
newBaseDir = './data/Cropped Dataset/'

dirs = [baseDir + setName + '/' +
        typeName + '/' for setName in sets for typeName in types]

# remove previous created data
try:
    shutil.rmtree(newBaseDir)
except:
    print('File not found')
# create new directories to put our cropped set
newDirs = [newBaseDir + setName + '/' +
           typeName + '/' for setName in sets for typeName in types]
for newDir in newDirs:
    try:
        os.makedirs(newDir, exist_ok=True)
    except OSError as error:
        print('Cannot make directory')


for DIR in dirs:
    out_DIR = DIR.replace('New Masks Dataset', 'Cropped Dataset')
    pics = os.listdir(DIR)
    for pic in pics:
        # print('handling pic:', DIR + pic)
        img = cv2.imread(DIR + pic)
        height = img.shape[0]
        width = img.shape[1]
        size = height * width

        # resizing speeds it up but misses a lot of faces.
        # gonna comment it since we have a limited datasize
        # if size > (500 ** 2):
        #     r = 500.0 / img.shape[1]
        #     dim = (500, int(img.shape[0] * r))
        #     img2 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        #     img = img2

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 2nd param: scaleFactor
        # values closer to 1.x = 1 are better, increasing chance to match
        # due to reducing size by x%
        # 3rd param: minNeighbors
        # Higher value = less detections, higher quality?
        faces = face_cascade.detectMultiScale(gray, 1.05, 6)
        eyesn = 0

        for (x, y, w, h) in faces:
            imgCrop = img[y:y+h, x:x+w]
            # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
            for (ex, ey, ew, eh) in eyes:
                # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                eyesn = eyesn + 1
            if eyesn >= 2:
                cv2.imwrite(out_DIR + pic, imgCrop)

        # cv2.imshow('img', imgCrop)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    print('Processed directory: ', DIR)

print("All images have been processed!!!")
cv2.destroyAllWindows()
cv2.destroyAllWindows()
