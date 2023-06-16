import os
import cv2
# names=["abhishek","aditya","akash","anirudh","ashish","chirag","hemanth","khushi","lekhana","nihith","paar","rohan","sheetal"]
names=["abhishek","aditya","akash","ashish","chirag","khushi","lekhana","nihith","paar","sheetal"]



for i in names:
    os_dir = f"E:/vscode/trial/val/{i}/"
    for idx, filename in enumerate(os.listdir(os_dir)):
        f = os_dir+filename
        r = os_dir+f"{i}_"+str(idx)+".jpg"
        print(f)
        if os.path.isfile(f):

            img = cv2.imread(f)
            # img = cv2.resize(img, [255, 255])
            cv2.imwrite(r, img)
            os.remove(f)
