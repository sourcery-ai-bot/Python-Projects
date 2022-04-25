"""
You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.

Sample Input
81239870

Sample Output
Valid

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1073/356

"""


import re
pattern = r"(^1|^8|^9)([0-9]{0,7}$)"
str=input("")
if match := re.search(pattern, str):
    print("Valid")
else:
    print("Invalid")