#!python3

"""
##### Problem 2
Calculate the factorial of a number. 

 4! does not mean 4 is excited, it's the notation for a factorial.
A factorial is a special operation in math that is used in probability 
and combination problems.  For example, if you have 4 people, the number
of ways that they can be lined up against the wall is 4!

A factorial is defined as:
5! = 1 * 2 * 3 * 4 * 5
5! = 120

3! = 1 * 2 * 3
3! = 6

inputs:
int number

outputs:
"xx! is yy" where xx is the integer entered and yy is the calculated answer

example:
Enter a number: 4
4! is 24
"""

number = input("")
factorial = 1
if int(number) >= 1:
    for i in range (1,int(number)+1):
        factorial = factorial * i
    print(number + "! is " + str(factorial))