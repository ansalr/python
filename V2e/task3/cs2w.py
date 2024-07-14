class Exercise2:
    
    def solution(self):
        
        tuples = []
        while True:

            user_input = input("Enter a tuple (name,age,height) or press Enter to stop: ")
            if not user_input:
                break
            name, age, height = user_input.split(',')
            tuples.append((name, age, height))

        sorted_tuples = []
        for _ in range(len(tuples)):
            min_tuple = tuples[0]
            min_index = 0
            for j in range(1, len(tuples)):
                if tuples[j][0] < min_tuple[0] or (tuples[j][0] == min_tuple[0] and tuples[j][1] < min_tuple[1]) or (tuples[j][0] == min_tuple[0] and tuples[j][1] == min_tuple[1] and tuples[j][2] < min_tuple[2]):
                    min_tuple = tuples[j]
                    min_index = j
            sorted_tuples.append(min_tuple)
            tuples.pop(min_index)

        print(sorted_tuples)
        
object1 = Exercise2()
object1.solution()