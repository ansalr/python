class Premide:

    def digram(self,n):
        for i in range(1,n+1):
            print('*'*i)
        while(i>0):
            i-=1
            print("*"*i)
            
n = 5
o1=Premide()
o1.digram(n)