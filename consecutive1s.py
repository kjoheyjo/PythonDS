#!/bin/python3

import sys


n = int(input().strip())
num = []
tempCount = 0
maxCount = 0
while(n>0):
    if n%2==0:
        num.append(0)
        if tempCount>maxCount:
            maxCount = tempCount
        tempCount = 0
    else:
        num.append(1)
        tempCount += 1
    n = int(n/2)
if tempCount>maxCount:
    maxCount = tempCount

print(maxCount)
