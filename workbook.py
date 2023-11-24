for i in range(10):
    print(i)

print("while loop")
w = 1
while w < 5:
    print(w)
    w = w+1




# {'ansal': 95, 'suresh': 90, 'raj': 99, 'ansalrobinson': 100}





















"""
def generate_opposite_string(s):
    opposite_string = ''.join(chr(ord('a') + ord('z') - ord(c)) for c in s)
    return opposite_string



T = int(input())
for _ in range(T):
    A = input().strip()
    B = generate_opposite_string(A)
    print(B)



c = 15
amount = 0
balance = c%10
cal = c//10
amount = cal
if balance == 0:
    cal = c/10
    print(int(cal))
    
else :
    if balance % 5 == 0 :
        amount +=1
        print(amount)
    else:
        print("-1") """



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