"""
Imputing missing values.

In the real world, you will often need to handle missing values. One way to impute (i.e., fill) the numerical column is to replace the null values with its mean.

Task
Given a list of numbers including some missing values, turn it into a pandas dataframe, impute the missing values with the mean, and finally return the dataframe.

Input Format
A list of numbers including one or more string "nan" to indicate a missing value.

Output Format
A list of imputed values where all values are rounded to its first decimal place.

Sample Input
3 4 5 3 4 4 nan

Sample Output
0 3.0
1 4.0
2 5.0
3 3.0
4 4.0
5 4.0
6 3.8
dtype: float64

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1093/105

"""

import numpy as np
import pandas as pd


lst = [float(x) if x != 'nan' else np.NaN for x in input().split()]


sample_df = pd.Series(lst)
mean_sample_df = sample_df.mean()
sample_df = sample_df.replace(np.nan, mean_sample_df)
sample_df = sample_df.round(1)
print(sample_df)