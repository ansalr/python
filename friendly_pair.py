def fact(n):
    sum1 = 0
    for i in range(1,(n//2)+1):
        if n%i==0:
            sum1+=i  
    return sum1-n
    
        
def main():
    num1,num2 = map(int,input().split())

    if fact(num1)==fact(num2):

        print("Friendly pair")
    else:
        print("Not a Friendly Pair")  

main()