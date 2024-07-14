class Cs2:
    
    def solution(self):
        
        data = [20,1,2,3,4,5,6]
        length = len(data)
        for i in range(1,length+1):
            print(data[-i],end=' ')
            
object1 = Cs2()
object1.solution()