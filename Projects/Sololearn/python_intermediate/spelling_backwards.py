"""
Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.

Sample Input
HELLO

Sample Output
O
L
L
E
H

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1158/1063

"""

def spell(txt):
    reversedtext = ""
    for i in txt:
        reversedtext = i + reversedtext
    for j in reversedtext:
        print(j)
        


txt = input()
spell(txt)
