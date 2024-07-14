class Cs5:
    def solution(self):
        
        list1 = ["M", "na", "i", "ke"]
        list2 = ["y", "me", "s", "lly"]
        result = []
        # result = [i + j for i, j in zip(list1, list2)]
        minlength = min(len(list1),len(list2))
        for i in range(minlength):
            result.append(list1[i] + list2[i])
        
        if len(list1) > len(list2):
            result.extend(list1[len(list2):])
        elif len(list2) > len(list1):
            result.extend(list2[len(list1):])

        print("Concatenated list:", result)

object1 = Cs5()
object1.solution()