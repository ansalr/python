class Cs6:
    
    def Solution(self):
        output = []
        list1 = ["Hello ", "take "]
        list2 = ["Dear", "Sir"]
        # output = [i+j for i in list1 for j in list2]
        for i in list1:
            for j in list2:
                output.append(i+j)
                    
        print(output)

object1 = Cs6()
object1.Solution()