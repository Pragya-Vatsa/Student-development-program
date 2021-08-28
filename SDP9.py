#WAP to reverse three digits i.e., 123 = 321
a = 123
rev_no = 0
while (a>0):
    remainder = a%10
    rev_no =  (rev_no * 10) + remainder  
    a = a // 10
print(rev_no)
