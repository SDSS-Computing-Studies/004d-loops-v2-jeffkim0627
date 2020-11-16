#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""
import math

width = int(input("Enter the width of a box: ").strip())
height = int(input("Enter the height of a box: "))
output = "*"
count = 0
if width < 10 and height < 10:
    while (math.ceil(width/2)) == (width/2) and (math.ceil(height/2)) == (height/2) and width < 10 and height < 10:
        output = output + str(width)
    while count < height:
        print(output*width)
        count = count + 1
else:
    print("Enter an integer value less than 10")

