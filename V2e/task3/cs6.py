class Exercise6:
    
    def solution(self):
        data = [[27,9,2,8,8,9,27,8],[1,18,2,1,18,4,4,1],[1,5,7,5,8,7,4,5],[1,2,3,5,8,4,4,3]] 
        uniqueList = 1
        for inplist in data:
            count = 0
            for num in inplist:
                if inplist.count(num) == 1:
                    count+=1
            uniqueList*=count
        print(uniqueList)
        
object1 = Exercise6()
object1.solution()