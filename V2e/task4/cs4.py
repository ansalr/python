class Cs4:
    
    def solution(self):
        
        inputList = [3,2,3,3,6,2,4,7]
        outputList = []
        for i in inputList:
            if i not in outputList:
                outputList.append(i)
        print(outputList)
        
object1 = Cs4()
object1.solution()