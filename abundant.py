def fact(n):
    sum1 = 0
    for i in range(1,(n//2)+1):
        if n%i==0:
            sum1+=i
    return sum1
        

def main():
    num1 = int(input())
    a = fact(num1)
    if a > num1:

        print(f"{num1} is an Abundant Number\nNum: {num1}\nSum: {a}\nAbundance: {a-num1}")
    else:
        print(f"{num1} is not a Abundant Number")  

main()