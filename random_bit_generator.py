import csv
import random
from shutil import copyfile
import os
from datetime import datetime

resolution = 16384
amp = 4
bits = resolution/16
freq = int(input("enter frequency (1:100Hz ; 2:1kHz ; 3:10kHz ; 4:100kHz ; 5:1MHz): "))

if freq == 1:
    freq = 10
elif freq == 2:
    freq = 1
elif freq == 3:
    freq = 0.1
elif freq == 2:
    freq = 0.01
else:
    freq = 1
name = str(input("enter name of test set: "))
os.mkdir(name)
step = float(freq) / resolution
r = resolution / bits
base = 0
time = 0.0
col = 14

today = datetime.now()
currentTime = today.strftime("%Y-%m-%d-%H-%M-%S")
with open(name+"/" + currentTime + "-RandomBits-FunctionGen.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    # writer.writerow(['Amplitude'])
    writer.writerow(['data length', resolution])
    writer.writerow(['frequency', 1])
    writer.writerow(['amp', amp])
    writer.writerow(['offset', 0])
    writer.writerow(['phase', 0])

    for i in range(0, 7):
        writer.writerow([])
    writer.writerow(['xpos', 'value'])

    last_bit = 0

    bits = int(bits)
    # make header
    bitArr = []
    new_Arr=[0]*200
    for i in range(0, 100):
        rand_bit = 0
        bitArr.append(rand_bit)
        for res in range(0, int(resolution / bits)):
            writer.writerow([time, rand_bit * amp])
            time += step
            col += 1
        base = base + r
        last_bit = rand_bit

    for i in range(0, bits - 101):
        rand_bit = random.randint(0, 1)
        bitArr.append(rand_bit)

        for res in range(0, int(resolution / bits)):
            writer.writerow([time, rand_bit * amp])
            time += step
            col += 1
        base = base + r
        last_bit = rand_bit
    for res in range(0, int(resolution / bits)):
        writer.writerow([time, amp])
        time += step
        col += 1
    base = base + r
    last_bit = rand_bit

    while col <= resolution + 13:
        writer.writerow([time, last_bit * amp])
        col += 1
        time += step

f.close()

for i in range(5):
        new_Arr+=[1,1,1,0,1]
        new_Arr+=[random.randint(0, 1) for x in range(195)]
        #new_Arr+=['Hey']
with open(name + "/RandomBits-RawBits.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    for x in new_Arr:
        writer.writerow([x])