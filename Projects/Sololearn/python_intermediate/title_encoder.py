"""
You are given a file named "books.txt" with book titles, each on a separate line.
To encode the book titles you need to take the first letters of each word in the title and combine them.
For example, for the book title "Game of Thrones" the encoded version should be "GoT".

Complete the program to read the book title from the file and output the encoded versions, each on a new line.

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1158/1066

"""


with open("/usercode/files/books.txt", "r") as file:
    booklist = []
    for a in file:
        filelist = list(a.split())
        d = "".join(i[0] for i in filelist)
        print(d)