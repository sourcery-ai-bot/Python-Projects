"""
You are making a registration form for a website.
The form has a name field, which should be more than 3 characters long.
Any name that has less than 4 characters is invalid.
Complete the code to take the name as input, and raise an exception if the name is invalid, outputting "Invalid Name". 
Output "Account Created" if the name is valid.

Sample Input
abc

Sample Output
Invalid Name

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1158/1065

"""

try:
    name = input()
    
    if len(name)>=4:
        print("Account Created")
    else:
        raise TypeError
except:
    print("Invalid Name")