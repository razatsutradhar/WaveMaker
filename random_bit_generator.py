import csv
import random
from shutil import copyfile
import os
from datetime import datetime


amp = float(input("enter amplitude in volts: "))
bits = int(input("enter number of bits(16, 8, 4, 2, 1)k: "))
resolution = 16384
if bits == 16:
    bits = resolution
elif bits == 8:
    bits = resolution / 2
elif bits == 4:
    bits = resolution / 4
elif bits == 2:
    bits = resolution / 8
else:
    bits = resolution / 16
name = str(input("enter name of test set: "))
os.mkdir(name)
copyfile('template.csv', str(name)+"/RandomBits-FunctionGen.csv")

step = 1.0 / resolution
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
        if i == 0:
            rand_bit = 1

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

with open(name + "/RandomBits-RawBits.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    for x in bitArr:
        writer.writerow([x])