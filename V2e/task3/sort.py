class Utility:
    
    def __init__(self):
        self.inputlist = []
        
    def solution(self):
    
        while True:
            user_input = input("Enter a tuple (name,age,height) or press Enter to stop: ")
            if not user_input:
                break
            name, age, height = user_input.split(',')
            self.inputlist.append((name, age, height))

            
class Exercise2:
    
    def solution(self):
        
        inplist = []
        while True:

            user_input = input("Enter a tuple (name,age,height) or press Enter to stop: ")
            if not user_input:
                break
            name, age, height = user_input.split(',')
            inplist.append((name, age, height))
        return self.arrange(inplist)

    def compare(self,t1,t2):
        pass
        #for t1 t2
            # if t1 != t2:
            #       return 1 if t1 > t2 else -1
            # else:
            #       continue 
        # if t1[0] != t2[0]:
        #     return 1 if t1[0] > t2[0] else -1
        # elif t1[1] != t2[1]:
        #     return 1 if t1[1] > t2[1] else -1
        # elif t1[2] != t2[2]:
        #     return 1 if t1[2] > t2[2] else -1
        # else:
        #     return 0
        
                

    def arrange(self,tuples):
        n = len(tuples)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.compare(tuples[j], tuples[j + 1]) > 0:
                    tuples[j], tuples[j + 1] = tuples[j + 1], tuples[j]
        print(tuples)
        
        
        
        
        
object1 = Exercise2()
object1.solution()