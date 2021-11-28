"""
You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
The function should be able to take a varying number of words as the argument.

Sample Input
this
is
great

Sample Output
this-is-great

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1073/358

"""

def concatenate(*args):
    text=""
    for i in range(len(args)):
        if i == len(args)-1:
            text += args[i]
        else:
            text += args[i] + "-"
    return text
    

print(concatenate("I", "love", "Python", "!"))