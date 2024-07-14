class Exercise10:
    
    def __init__(self) -> None:
        self.output = {}
        
    def product1(self,output):
        product = 1
        for key in output.keys():
            if(str(key).isdigit() == True):
                product*=int(key)
            else:
                product*= int(key[0])
        print(product)        
                              
    def solution(self):
                
        data = [[27,9,2,8,8,9,27,8],[1,18,2,1,18,4,4,6,1],[1,5,7,5,8,7,4,5],[1,2,3,5,8,4,4,3]]
        output = {}
        product = 1
        for inplist in range(len(data)):
            repeat = 0
            alphabet = 97
            for value in range(len(data[inplist])):
                if (data[inplist]).count(data[inplist][value]) == 1:
                    
                    product*=(inplist+1)
                    if repeat == 0:
                        output[inplist+1]=data[inplist][value]
                        repeat+=1
                    else:
                        output[str(inplist+1)+chr(alphabet)]=data[inplist][value]
                        repeat+=1
                        alphabet+=1

        self.product1(output)

        
object1 = Exercise10()
object1.solution()