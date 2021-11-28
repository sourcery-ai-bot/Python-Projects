"""
You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.

For example, if the books.txt file contains:
Some book
Another book

Your program should output:
S9
A12

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1073/353

"""

file = open("/usercode/files/books.txt", "r")

book =[]
for i in file:
    if "G" == i[0]:
        book.append(i)
    else:
        i = i[:-1]
        book.append(i)

line = []
for i in book:
    i = i[0] + str(len(i))
    line.append(i)

for i in line:
    print(i)
file.close()