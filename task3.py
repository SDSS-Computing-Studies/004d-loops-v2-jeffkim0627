#! python3
"""
##### Task 3
Given a typle that contains a series of numbers, list all the ones that are
divisible by 5
(2 points)

inputs:
none

outputs:
list of numbers
25
10
30
75
20
"""
import math

numList = [25, 8, 10, 11, 33, 30, 51, 75, 63, 14, 20, 99]

for i in numList:
    if (int(numList) / 5) == (math.ceil(int(numList) / 5)):
        print(i)
    else :
        break