import cv2
import numpy as np
from pathlib import Path
import csv

lower = np.array([0, 215, 139])
higher = np.array([108, 255, 255])
p = Path('./data')
lst = [str(x) for x in p.iterdir()]
obj_data = [[(0, 0), (56, 39)], [(0, 39), (56, 74)], [(0, 74), (56, 115)], [(0, 115), (56, 158)]]
lst_img = []
my_data = []
for im in lst:
    frame = cv2.imread(im)
    for images in obj_data:
        roi = frame[images[0][1]:images[1][1], images[0][0]:images[1][0]]
        im = cv2.rectangle(frame, images[0], images[1], (255, 255, 255), 2)
        cat_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(cat_hsv, lower, higher)
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        if(len(cnts) > 0):
            lst_img.append(1)
        else:
            lst_img.append(0)
    my_data.append(lst_img.copy())
    lst_img.clear()
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(my_data)