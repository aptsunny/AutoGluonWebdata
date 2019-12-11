import csv
import os
import shutil
import string
from gluoncv.utils import makedirs

csvfile = "labels.csv"
pic_path = "images/"
train_path = "train/"

csvfile = open(csvfile, 'r')
data = []
for line in csvfile:
    data.append(list(line.strip().split(',')))

for i in range(len(data)):
    if i == 0:
        continue
    if i >= 1:
        cl = data[i][1]
        name = data[i][0]
        path = pic_path + str(name) + '.jpg'

        isExists = os.path.exists(path)
        if (isExists):

            if not os.path.exists(train_path + cl):
                os.makedirs(train_path + cl)

            newpath = train_path + cl + '/' + str(name) + '.jpg'
            shutil.copyfile(path, newpath)
            print(str(name) + ',success')
        else:
            print(str(name) + ",not here")

