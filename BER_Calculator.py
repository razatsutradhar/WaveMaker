import csv
import math
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


# end of function lcs


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y))

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

index = 0
for x in data2:
    if x == 1:
        break
    else:
        index += 1
data2 = data2[index:]

print(data1)
print(data2)
if len(data1) > len(data2):
    diff = len(data1) - len(data2)
    for i in range(0, diff):
        data2.append(-1)

if len(data2) > len(data1):
    diff = len(data2) - len(data1)
    for i in range(0, diff):
        data1.append(-1)
# print(data1)
# print(data2)
point = 0
total = len(data1)
print(lcs(data1,data2)/total)

for x in range(0, len(data1)):
    if data1[x] == data2[x]:
        point += 1

#print(point / total)
