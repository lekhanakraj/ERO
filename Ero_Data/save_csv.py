import os
import csv
abi="E:/vscode/trial/val/abhishek/"
adi="E:/vscode/trial/val/aditya/"
ak="E:/vscode/trial/val/akash/"
ani="E:/vscode/trial/val/anirudh/"
ash="E:/vscode/trial/val/ashish/"
chi="E:/vscode/trial/val/chirag/"
hemanth="E:/vscode/trial/val/hemanth/"
khushi="E:/vscode/trial/val/khushi/"
lekhana="E:/vscode/trial/val/lekhana/"
nihith="E:/vscode/trial/val/nihith/"
paa="E:/vscode/trial/val/paar/"
rohan="E:/vscode/trial/val/rohan/"
she="E:/vscode/trial/val/sheetal/"
filename=[]
label=[]
dicts={}
rows=[]
for file in os.listdir(abi):
    f=abi+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Abhishek SJ")
for file in os.listdir(adi):
    f=adi+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Aditya VSM")
for file in os.listdir(ak):
    f=ak+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Akash")
for file in os.listdir(ani):
    f=ani+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Aniruddh Bhardwaj")
for file in os.listdir(ash):
    f=ash+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Ashish")
for file in os.listdir(chi):
    f=chi+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Chirag")
for file in os.listdir(hemanth):
    f=hemanth+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Hemanth")
for file in os.listdir(khushi):
    f=khushi+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Khushi")
for file in os.listdir(lekhana):
    f=lekhana+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Lekhana")
for file in os.listdir(nihith):
    f=nihith+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Nihith")
for file in os.listdir(paa):
    f=paa+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Paar")
for file in os.listdir(rohan):
    f=rohan+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Rohan")
for file in os.listdir(she):
    f=she+file
    print(f)
    if os.path.isfile(f):
        filename.append(file)
        label.append("Sheetal")        

for i in range(len(filename)):
    dicts[filename[i]]=label[i]
rows=list(dicts.items())
print(rows)
fieldnames = ['filename','name']

with open('val.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(fieldnames)

    # write multiple rows
    writer.writerows(rows)