class Number:
    
    def calc(self,n):
        n = 5
        print(0)
        for i in range(1,n):
            print(0,end=' ')
            a  = 3
            p = 0
            for j in range (i):
                sum = p+a
                print(sum,end=' ')
                p = sum
                a +=2
            print()

        i = n-1
        while (i>0):
            i-=1
            print(0,end=' ')
            a  = 3
            p = 0
            for j in range (i):
                sum = p+a
                print(sum,end=' ')
                p = sum
                a +=2
            print()
n = 5           
o1=Number()
o1.calc(n)