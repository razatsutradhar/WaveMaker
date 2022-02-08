import csv
import math
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
file1 = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
file2 = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

with open(file1, newline='') as csvfile:
    temp = list(csv.reader(csvfile))
    data1 = [int(x[0]) for x in temp]
    csvfile.close()
with open(file2, newline='') as csvfile:
    temp = list(csv.reader(csvfile))
    data2 = [int(x[0]) for x in temp]
    csvfile.close()

index = 0

for x in data1:
    if x == 1:
        break
    else:
        index += 1
data1 = data1[index:]
data1 = data1[1:]
index = 0
for x in data2:
    if x == 1:
        break
    else:
        index += 1
data2 = data2[index:]

if len(data1) > len(data2):
    diff = len(data1) - len(data2)
    for i in range(0, diff):
        data2.append(-1)

if len(data2) > len(data1):
    diff = len(data2) - len(data1)
    for i in range(0, diff):
        data1.append(-1)
print(data1)
print(data2)
point = 0
total = len(data1)
for x in range(0, len(data1)):
    if data1[x] == data2[x]:
        point += 1

print(point / total)
