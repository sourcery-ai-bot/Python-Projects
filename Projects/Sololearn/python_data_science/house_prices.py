"""
You are given an array that represents house prices.
Calculate and output the percentage of houses that are within one standard deviation from the mean.

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1161/1156

"""

import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
meand = np.mean(data)
stdd = np.std(data)
nsatisfied = 0
for i in data:
    if meand - stdd <= i and i <= meand + stdd:
        nsatisfied += 1
print((nsatisfied/len(data))*100)