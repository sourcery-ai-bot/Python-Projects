"""
You are making a program to analyze text.
Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.

Sample Input:
hello
l

Sample Output:
40

The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40.

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1159/1098

"""

word1 = input()
letter1 = input()
a = 0

for i in word1:
    if i in letter1:
        a += 1

percent1 = (a/len(word1))*100
percent1 = int(percent1)
print(percent1)