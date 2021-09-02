# WAP to enter 5 integer number and find min number (using simple if)
num = [1, 2, 3, 4, 5]
min = num[0]
for i in num:
    if(min > i):
        min = i
print(min)
