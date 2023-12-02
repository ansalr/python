# problem statement
# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def cal_binary(value):
    b = bin(value)[2:]
    return f"{b}"

def max_zero(value):
    count ,max_0= 0,0
    for i in value:
        if i == '0':
            count += 1
            
        else:
            max_0 = max(count,max_0)
            count = 0
    return max_0
                    

inpt = int(input())
b1 = cal_binary(inpt)
print(b1)
print(max_zero(b1))

