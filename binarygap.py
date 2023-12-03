# problem statement
# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def cal_binary(value):
    b = bin(value)[2:]
    return f"{b}"

def max_zero(value):
    count ,max_0= 0,0
    for i in list(value):
        if i == '0':
            count += 1
            
        else:
            max_0 = max(count,max_0)
            count = 0
    return max_0
                    




def solution(N):
    b1 = cal_binary(N)
    return max_zero(b1)

