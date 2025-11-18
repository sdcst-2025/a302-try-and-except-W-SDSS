#!python3

# Reciprocal
# have the user enter numbers and determine the 
# reciprocal of each number as a decimal and print it.
# use the try/except to find any invalid values and display
# the error message

#sample output:
"""
Enter a number: 0
The reciprocal of 0 does not exist
Enter a number: 1
The reciprocal of 1 is 1.0
Enter a number: 2
The reciprocal of 2 is 0.5
Enter a number: 3
The reciprocal of 3 is 0.3333333333333333
Enter a number: 4
The reciprocal of 4 is 0.25
"""

num = input("Enter a number: ")

try:
    number = float(num)
except ValueError:
    print("That is not a valid number")
else:
    try:
        recip = 1 / number
        print(f"The reciprocal of {num} is {recip}")
    except recip == 0:
        print(f"The reciprocal of {num} does not exist")

#naositayo
