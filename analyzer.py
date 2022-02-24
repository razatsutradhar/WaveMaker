import csv
import math
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename, askdirectory

def rearrangeArray(arr, original):
    maxIndex = arr.index(max(arr))
    # print("temp: ")
    temp = arr[0:maxIndex]
    # print(temp)
    arr = arr[maxIndex:]
    # print("arr")
    # print(arr)
    if original[0] != original[len(original)-1]:
        for i in temp:
            arr.append(i)
    else:
        arr[len(arr)-1] = arr[len(arr)-1] + temp[0]
        for i in range(1, len(temp)-1):
            arr.append(temp[i])
    return arr


def compress(bitArr, scale):
    compressedList = []
    lastbit = 0
    streak = 0
    for x in bitArr:
        if x == lastbit:
            streak += 1
        else:
            compressedList.append(round(streak/scale))
            streak = 1
            lastbit = x
    return compressedList


def getSegments(arr):
    segments = []
    headderLen = arr[0]
    last = 0
    for i in range(1, len(arr)-1):
        if arr[i] > headderLen*0.95 or i == len(arr)-1:
            segments.append(arr[last:i-1])
            last=i
    return segments



def csv_to_arr(filepath):
    with open(filepath, newline='') as csvfile:
        temp = list(csv.reader(csvfile))
        data1 = [int(x[0]) for x in temp]
        csvfile.close()
    return data1


Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askdirectory()  # show an "Open" dialog box and return the path to the selected file
oscData = filename+'/OscilloscopeData.csv'
print(filename)

oscLen = int(input("len of osc data: "))
freq = int(input("frequeny of function gen: "))


#read the oscilloscope data
with open(oscData, newline='') as csvfile:
    data = list(csv.reader(csvfile))[0]
csvfile.close()

# print("Read Data from file")

data = [float(d) for d in data]

# print("Turned all ints into floats")

avg = sum(data) / (len(data) - 100)

# print("Found Avg")
bitArr = []
for x in data:
    if x > avg:
        bitArr.append(1)
    else:
        bitArr.append(0)
# print(bitArr)
# print("Turned volts to 1's and 0's")
compressedList = compress(bitArr, oscLen/freq)

# print("Compressed")
# print(compressedList)
compressedList = rearrangeArray(compressedList, bitArr)
# print("rearranged")
print(compressedList)

sg = getSegments(compressedList)
print("segments")
print(sg[0])
# print(sum(compressedList,1))
#
# print("original data (compressed): ")
original = compress(csv_to_arr(filename+'/RandomBits-RawBits.csv'),1)
# print(original)
# print(sum(original))
#
# compressedBits = compress(bitArr,1000/8)
#
# a = rearrangeArray(compressedBits, bitArr)
print("bit array (compressed): ")
print(original)
finished_list = []
starter = 0
for x in sg[0]:
    for y in range (0, x):
        finished_list.append(starter)
    if starter == 0:
        starter = 1
    else:
        starter = 0

with open(filename+"/CleanedData.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    for x in finished_list:
        writer.writerow([x])

f.close()
print(len(data))
print(len(csv_to_arr(filename+'/RandomBits-RawBits.csv')))

