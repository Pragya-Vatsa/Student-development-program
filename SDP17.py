# WAP to find palindrome number
num = 131
sum = 0
rev = 0
temp = num
while (temp > 0):
    sum = temp % 10
    rev = rev * 10 + sum 
    temp //= 10
if num == rev:
    print(num, "is a Palindrome number")
else:
    print(num, "is not a Palindrome number")
