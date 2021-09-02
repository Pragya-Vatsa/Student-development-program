# WAP to enter 5 integer number and find max number (using simple if)
num = [1, 2, 3, 4, 5]
max = num[0]
for i in num:
    if(max < i):
        max = i
print(max)
