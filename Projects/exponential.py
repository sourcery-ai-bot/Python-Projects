one = 1000000
day = input()
two = 0.01
for i in range(30):
    two = two * 2
    if i == day:
        print(two)
    
print(two)