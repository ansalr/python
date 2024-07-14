class Exercise4:
    
    def solution(self):
        
        tuples = []
        while True:

            user_input = input("Enter a tuple (name, age, height,Gender) or press Enter to stop: ")
            if not user_input:
                break
            name, age, score, gender = user_input.split(',')
            tuples.append((name, age, score, gender ))

        sorted_tuples = []
        for i in range(len(tuples)):
            min_tuple = tuples[0]
            min_index = 0
            for j in range(1, len(tuples)):
                if tuples[j][3] < min_tuple[3] or (tuples[j][3] == min_tuple[3] and tuples[j][0] < min_tuple[0]) or (tuples[j][3] == min_tuple[3] and tuples[j][0] == min_tuple[0] and tuples[j][1] < min_tuple[1]) or (tuples[j][3] == min_tuple[3] and tuples[j][0] == min_tuple[0] and tuples[j][1] == min_tuple[1] and tuples[j][2] < min_tuple[2]):
                    min_tuple = tuples[j]
                    min_index = j
            sorted_tuples.append(min_tuple)
            tuples.pop(min_index)

        print(sorted_tuples)
        
object1 = Exercise4()
object1.solution()

"""
John,20,90,M
 Angel,19,79,F
 Jony, 17,93,M
 Reny,19,80,F
 Jony, 17, 91,M
 Reny,28,85,F
 Jason,21,85,F
   
"""