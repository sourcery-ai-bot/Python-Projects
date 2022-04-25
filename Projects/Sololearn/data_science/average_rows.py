"""
In a matrix, or 2-d array X, the averages (or means) of the elements of rows is called row means.

Task
Given a 2D array, return the rowmeans.

Input Format
First line: two integers separated by spaces, the first indicates the rows of matrix X (n) and the second indicates the columns of X (p)
Next n lines: values of the row in X

Output Format
An numpy 1d array of values rounded to the second decimal.

2 2
1.5 1
2 2.9

Sample Output
[1.25 2.45]

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1093/111

"""


n, p = [int(x) for x in input().split()]
array1 = [input().split() for _ in range(n)]

import numpy as np

arr1 = np.array(array1)
arr1 = arr1.astype(np.float16)
mean1 = arr1.mean(axis=1)
mean1 = mean1.round(2)
print(mean1)

