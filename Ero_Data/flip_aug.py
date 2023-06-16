import cv2
import glob
from PIL import Image
import os

black_white = []
names=["abhishek","aditya","akash","anirudh","ashish","chirag","hemanth","khushi","lekhana","nihith","paar","rohan","sheetal"]

# dir = "E:/face_rec/nihith/"
for i in names:
    images_path = f"E:/vscode/trial/train/{i}/"
    for img1 in os.listdir(images_path):

        img = cv2.imread(images_path+img1)
        img_vh = cv2.flip(img, 1)
        cv2.imwrite(images_path+f"{img1}_filp.jpg", img_vh)
        cv2.waitKey(0)