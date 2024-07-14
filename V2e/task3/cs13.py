class Exercise13:
    
    def __init__(self) -> None:
        self.list1 = ["M", "comp", "na", "i", "v2e"]
        self.list2 = ["y", "any", "me", "s", "Technologies"]
        self.result = []

    def solution(self):
        # result = [i + j for i, j in zip(list1, list2)]
        small= min(len(self.list1),len(self.list2))
        for i in range(small):
            self.result.append(self.list1[i]+self.list2[i])

        if len(self.list1) > len(self.list2):
            self.result.extend(self.list1[len(self.list2):])
        elif len(self.list2) > len(self.list1):
            self.result.extend(self.list2[len(self.list1):])

        print("Concatenated list:", self.result)

        final_result = self.result[-2:][::-1] + self.result[:-2]

        print("Final list:", final_result)
        
object1 = Exercise13()
object1.solution()