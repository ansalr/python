class Premide:
    def __init__(self) -> None:
        self.num = 49
        self.l = 64

    def digram(self,n):
        for i in range(n+1):
            letter = chr(self.l)
            print(letter*i)
            print(str(i)*i)
            self.l+=1
            
n = 5
o1=Premide()
o1.digram(n)
