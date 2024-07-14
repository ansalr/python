class Exercise7:
    
    def solution(self):
                
        data = [[27,9,2,8,8,9,27,8],[1,18,18,18,19,4,4,1],[1,5,5,5,8,7,4,5],[1,2,3,5,8,4,4,3],[18,27,63,36,27,27,
        27,1,5],[3,5,8,4,4,4,2,15,15,151]]
        newlist = []
        for inplist in range(len(data)):
            for value in range((len(data[inplist]))-2):
                if ((data[inplist][value]) == ((data[inplist][value+1])) == ((data[inplist][value+2]))):
                    newlist+=[value,value+1,value+2]
        
        print(newlist)
        
object1 = Exercise7()
object1.solution()
