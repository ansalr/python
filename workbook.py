# print(f"{(lambda a,b:a*b)(4,3)}")
# Python program to
# demonstrate protected members

# Python program to
# demonstrate private members

# Creating a Derived class
""" 
a = int(input())
b = 0
for i in range(a):
    c = int(input())
    b+=c 


print(b*a) 
        
n = []
for i in range(5):
    n+=[i]
print(n)





 import datetime as datetime
today = datetime.datetime.now()
print(today.day)
print(today.month)
print(today.year)
print(today.hour-12)
print(today.minute)
print(today.second)  """

import random
num1=random.randint(450,950)-450
num2=random.randint(450,950)-450
avg=(num1+num2)/2
print("the number ",num1,num2)
print(avg)