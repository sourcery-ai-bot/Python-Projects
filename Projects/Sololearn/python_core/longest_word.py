"""
Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1073/354

"""

txt = input()
splitted = txt.split()
n = len(splitted)
for i in range(n):
    alreadysorted=True
    for j in range(n-i-1):
        if len(splitted[j])>len(splitted[j+1]):
            splitted[j], splitted[j+1] = splitted[j+1], splitted[j]
            alreadysorted=False
    if alreadysorted:
        break

print(splitted[-1])
        