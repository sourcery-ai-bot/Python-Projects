"""
You are making a Celsius to Fahrenheit converter.
Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

Sample Input
36

Sample Output
96.8

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1073/352

"""

celsius = int(input())

def conv(c):
    return ((9/5)*c)+32
    

fahrenheit = conv(celsius)
print(fahrenheit)