#!python3 

"""
##### Task 1
Ask the user to enter an integer.
Print the multiplication tables up to 12 for that number
using a for loop instead of a while loop.
(2 points)

inputs:
int number

outputs:
multiples of that number

example:
Enter number:4
4 8 12 16 20 24 28 32 36 40 44 48
"""
num = int(input("Enter number: "))

nums = [str(num*1), str(num*2), str(num*3), str(num*4), str(num*5), str(num*6), str(num*7), str(num*8), str(num*9), str(num*10), str(num*11), str(num*12)]


output = ""
for i in range(0,1):
    output = output + str(nums)
print(output)