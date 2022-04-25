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
    return "".join(
        args[i] if i == len(args) - 1 else f"{args[i]}-"
        for i in range(len(args))
    )
    

print(concatenate("I", "love", "Python", "!"))