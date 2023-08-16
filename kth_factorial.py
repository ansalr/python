def factorial(k,n):
    n_term = k/2
    
    fact = []
    for i in range(1,int(n_term)+1):
        if k%i==0:
            fact.append(i)
    fact.append(k)
    
    if n>len(fact):
        return 1
    else:
        return fact[-n]

    



k,n=map(int,input().split())
output = factorial(k,n)
print(output)