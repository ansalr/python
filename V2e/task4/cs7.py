class Cs7:
    def solution(self):
        
        list1 = [10, 20, 30, 40]
        list2 = [100, 200, 300, 400]
        if len(list1) == len(list2):
            for i in range(len(list2)):
                print(f"{list1[i]} {list2[-(i+1)]}")
                
object1 = Cs7()
object1.solution()