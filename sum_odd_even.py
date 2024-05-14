# find odd even diffrence

input1 = 5
input2 = [10 , 11, 7, 12, 14]
odd, even = 0,0 
for i in input2:
    if i%2 == 0:
        even+=i
    else:
        odd+=i
print(odd-even)
