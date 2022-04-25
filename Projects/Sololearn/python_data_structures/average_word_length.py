"""
Given a sentence as input, calculate and output the average word length of that sentence.
To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.

Sample Input:
this is some text

Sample Output:
3.5

Explanation: There are 4 words in the given input, with a total of 14 letters, so the average length will be: 14/4 = 3.5

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1159/1102

"""


text = input()
list1 = list(text.split())
a = sum(i != " " for i in text)
print(a/len(list1))