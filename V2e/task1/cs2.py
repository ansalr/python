def password(pas):
    nl = []
    for k in pas:
        p = list(k)
        sl = 0
        num = 0
        ca = 0
        sc = 0
        
        if len(p)>10:
            pass
        else:
            for i in p:
                n=ord(i)
                if (n>=97 and n<=122):
                    sl+=1
                elif(n>=48 and n<=57):
                    num+=1
                elif(n>=65 and n<=90):
                    ca+=1
                elif((n>=33 and n<=47) or(n>=58 and n<=64) or(n>=91 and n<=96) ):
                    sc+=1
            if (sl>=2 and sl<=5):
                if(num>=3 and num<=4):
                    if(ca>=1 and ca<=2):
                        if(sc>=1 and sc<=2):
                            nl.append(k)
    print(*nl)      
    
    
pas = ['aa876A*','andjhgh','aa876KA$','akdup$%A543','ad375B&']
password(pas)
        