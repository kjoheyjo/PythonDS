#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
tempSum = 0
maxSum = -100
for i in range(1,5):
    for j in range(1,5):
        middle = arr[i][j]
        tempSum = middle
        for l in [i-1,i+1]:
            for k in range(j-1,j+2):
                tempSum = tempSum + arr[l][k]
        
        if tempSum>maxSum:
            maxSum = tempSum

           
print(maxSum)            
        