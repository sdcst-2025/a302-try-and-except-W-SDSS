#!python 3

# Square root of a number

# Have the user enter in a number.  Use a try-except to see if the input
# is a valid number.  Determine the square root and use a try-except to
# catch exceptions if the number can not be square rooted
# note: Use the math.sqrt() function to determine a square root
# rather than number**(0.5) as we need to catch complex numbers as
# exceptions

"""
Sample Output
Enter a number:x
That is not a valid number
There is no square root   
Enter a number:-1
There is no square root
Enter a number:3       
The square root of 3.0 is 1.7320508075688772
"""
num = input("Enter a number: ")

import math

try:
    num = float(num)
except ValueError:
    print("That is not a valid number")
    print("There is no square root")
else:
    try:
        re = math.sqrt(num)
        print(f"The sqare root of {num} is {re}")
    except ValueError:
        print("There is no sqare root")
