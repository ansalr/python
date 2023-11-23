n = 1000000000
a = 0
b = 1
for i in range(2,n):
      
    c = a+b
    a = b
    b = c
print(c)


"""
c = ")("
c.split()
string = list(c)
value = []
index1 = []

for i in string:
    if i == '(':
        value.append('a')
    elif i == ')':
        value.append('b')

print(value)

for _ in range(((len(string))%2)+1):
    index1 = []
    for i in range(len(value)-1):
        value1 = value[i]
        value2 = value[i+1]
        
        if value1 == 'a' and value2 == 'b':
            index1.append(i)
            index1.append(i+1)
    
    index1.sort(reverse = True)
            
    print(index1)
    for i in index1:
        value.pop(i)
    
print(value)
print("number of ( : ",value.count('a'))
print("number of ) : ",value.count('b'))

        
        
    





"""






















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
print(today.second)  

import random
num1=random.randint(450,950)-450
num2=random.randint(450,950)-450
avg=(num1+num2)/2
print("the number ",num1,num2)
print(avg)
"""
