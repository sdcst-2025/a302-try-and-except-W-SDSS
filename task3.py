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
num = int(input("Enter a number: "))

import math
root = math.sqrt(num)

try:
    root = True
    print(f"The squar root of {num} is {root}")
except:
    root = False
    print("That is not a valid number")
    print("There is no square root")

    #yoku wakaran