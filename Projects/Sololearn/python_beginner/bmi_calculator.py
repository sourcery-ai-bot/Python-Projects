"""
Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. 
It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, 
by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

Sample Input
85
1.9

Sample Output
Normal

Here is the link for original project site
https://www.sololearn.com/learning/eom-project/1157/1020

"""

weight = float(input())
height = float(input())
bmi = weight/height**2
if bmi>30:
    print("Obesity")
elif bmi>=25:
    print("Overweight")
elif bmi>=18.5:
    print("Normal")
else:
    print("Underweight")

