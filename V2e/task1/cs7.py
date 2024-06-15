class Number:
    
    def calc(self,l):
        nl = []
        for i in l:
            if i>0 and i<= 26:
                if i%2 ==0:
                    if i not in  [1,5,9,15,21]:
                        nl.append(i)
        print(nl)
        
l = [22,5,5,20,31,5,3,8,28,30,14,15,12,15,7,9,5,19,27]
o1=Number()
o1.calc(l)
