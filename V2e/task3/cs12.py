class Exercise12:
    
    def __init__(self) -> None:
        self.output = []
        
    def solution(self):
        
        for i in range(12,45):
            if i%2 == 0:
                self.output.append(i)
        for j in range(1,len(self.output)):
            print(self.output[-j],end=',')
        
object1 = Exercise12()
object1.solution()