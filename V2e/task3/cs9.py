class Exercise9:
        
    def solution(self):
        set1 = {11,10, 20, 30, 40, 50}
        set2 = {25,30, 40, 50, 60, 70}
        set3 = {3,9, 20, 30, 40, 50,20}
        
        unique_elements = (set1 - set2 - set3) | (set2 - set1 - set3) | (set3 - set1 - set2)
        sorted_unique_elements = sorted(list(unique_elements))
        print(sorted_unique_elements)
        
object1 = Exercise9()
object1.solution()