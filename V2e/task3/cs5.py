class Exercise5:
    
    def Solution(self):
        inputText = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."


        words = inputText.split()
        frequency = {}

        for word in words:
            if word not in frequency:
                frequency[word] = 1
            else:
                frequency[word] += 1


        sorted_keys = sorted(frequency.keys())

        for key in sorted_keys:
            print(f"{key}:{frequency[key]}")
            
object1 = Exercise5()
object1.Solution()