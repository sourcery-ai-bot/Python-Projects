"""
The given code includes a list of heights for various basketball players.
You need to calculate and output how many players are in the range of one standard deviation from the mean.

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1161/1151

"""

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
meanplayers = sum(players)/len(players)
variance = 0
for i in players:
    variance += (i-meanplayers)**2
variance = variance/len(players)
variance = variance ** 0.5
inrangeplayers=0
for i in players:
    if (meanplayers-variance)<i and i<(meanplayers + variance):
        inrangeplayers += 1
print(inrangeplayers)