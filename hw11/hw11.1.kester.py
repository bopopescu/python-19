#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #11 WOOT!!!
# November 24, 2014
# Functional programming
# Script 1
#---------------------------------------------------------

def reversi(num):
    return int(str(num)[::-1]) == num

maxRev = 0
numString = None

for x in range(999, 99, -1):
    for y in range(x, 99, -1):
        num = x * y
        if reversi(num) and num > maxRev:
            maxRev = num
            numString = str(x) + " x " + str(y)

print numString + " = " + str(maxRev)