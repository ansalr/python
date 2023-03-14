a = [25, 22, 39, 36, 52]
b = []
c = len(a)
d = 0


while d<=c:
    f= len(a)
    if f !=0:
        d+=1
        e = max(a)
        b.append(e)
        a.remove(e)
        
    else:
        print(b)
        break
    
   





      