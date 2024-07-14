class Cs1:
    
    def solution(self):
                
        data = [2,3,4,12,5,6,11]
        maxnumber = 0
        for i in data:
            if i > maxnumber:
                maxnumber = i
        print(maxnumber)
    
object1 = Cs1()
object1.solution()