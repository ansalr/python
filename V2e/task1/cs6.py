class Number:
    
    def calc(self,l):
        nl=[]
        for i in l:
            if i<=144:
                return nl
            else:
                if i>1200:
                    pass
                else:
                    if i%12==0:
                        nl.append(i)
        return nl 
        
        
l = [1200,1201,180,1000,1001,140,145,150]
o1=Number()
print(o1.calc(l))
