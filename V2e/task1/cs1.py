class Number:
    def __init__(self) -> None:
        self.nlist=[]
        self.new_d={}
        
    def calc(self,inp):
        for i in range(1,len(inp),2):
            self.nlist.append(inp[i])
        print(self.nlist)
        
        for i in range(0,int(len(inp)/2),2):
            self.new_d[inp[i]]=inp[i+1]
            
        print(self.new_d)
                
        
inp = list(map(str,input().split(',')))
o1=Number()
o1.calc(inp)