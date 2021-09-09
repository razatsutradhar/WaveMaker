import csv
import math
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename, askdirectory

def findHeader(arr, headerLen, resolution):
    indexes = []
    largestStreak = -1
    before = -1
    next = -1
    for i in range(0, len(arr), headerLen-1):
        if arr[i] == 0:
            before = i
            next = i
            while next < len(arr) and arr[next] == 0:
                next += 1
            while before > 0 and arr[before] == 0:
                before -= 1
            if (next - before) > largestStreak:
                indexes = [before+1, next]
                largestStreak = (next-before)


    return indexes

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askdirectory()  # show an "Open" dialog box and return the path to the selected file
oscData = filename+'/OscilloscopeData.csv'
print(filename)

bitRate = 1000 #number of bits in raw data
frameRate = 1000000
resolution = frameRate / bitRate


with open(oscData, newline='') as csvfile:
    data = list(csv.reader(csvfile))[0]
csvfile.close()

print("Read Data from file")

data = [float(d) for d in data]

print("Turned all ints into floats")

avg = sum(data) / (len(data) - 100)

print("Found Avg")
bitArr = []
for x in data:
    if x > avg:
        bitArr.append(1)
    else:
        bitArr.append(0)

print("Turned volts to 1's and 0's")
indexes = findHeader(bitArr, 100, 1000)
print(indexes)
print("found header")
temp = bitArr[0:indexes[0]]
bitArr = bitArr[indexes[0]:]
print(len(temp))
for x in temp:
    bitArr.append(x)

print("Appended stuff in the headder in the beginning")
compressedList = []
lastbit = 0
streak = 0
for x in bitArr:
    if x == lastbit:
        streak += 1
    else:
        compressedList.append((streak/(frameRate/bitRate)))
        streak = 1
        lastbit = x
print("Compressed")
print(compressedList)

finished_list = []
starter = 0
for x in compressedList:
    for y in range (0, round(x)):
        finished_list.append(starter)
    if starter == 0:
        starter = 1
    else:
        starter = 0
print(len(finished_list))

with open(filename+"/CleanedData.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    for x in finished_list:
        writer.writerow([x])

f.close()


