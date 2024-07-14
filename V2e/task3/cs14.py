class Concatenate:
    
    def __init__(self) -> None:
        
        self.list1 = ["Hello ", "take "]
        self.list2 = ["Dear", "Coffee"]
        self.result = []
        self.final_result = []
        
    def solution(self):

# result = [i + j for i in list1 for j in list2]

        for j in self.list2:
            for i in self.list1:
                self.result.append(i+j)
        print("Concatenated list:", self.result)


        for word in self.result:
            if self.final_result.count(word) < 1:
                self.final_result.append(word)

        print("Final list:", self.final_result)
        
object1 = Concatenate()
object1.solution()