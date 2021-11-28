"""
You’re working on a search engine. Watch your back Google!

The given code takes a text and a word as input and passes them to a function called search().

The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

Sample Input
"This is awesome"
"awesome"

Sample Output
Word found

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1157/1022

"""

def search(text,word):
    if word in text:
        return "Word found"
    else:
        return "Word not found"
text = input()
word = input()

print(search(text, word))