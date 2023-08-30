def hcf():
    num1,num2 = map(int,input().split())
    
    i = 1
    while ( i < num1 and i < num2 ):
    
        if ( num1%i == 0 == num2%i ):
    
            hcf = i
        i +=1
    
    print(hcf)

hcf()