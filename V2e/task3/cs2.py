class Exercise2:
    
    def get_input(self):
            input_tuples = []
            while True:
                try:
                    input_str = input("Enter a tuple (name, age, height) or 'done' to finish: ")
                    if input_str.lower() == "done":
                        break
                    name, age, height = input_str.split(",")
                    input_tuples.append((name.strip(), int(age.strip()), int(height.strip())))
                    print(input_tuples)
                except ValueError:
                    print("Invalid input. Please enter a valid tuple (name, age, height).")
            return input_tuples
            
    def sort_tuples(self,input_tuples):
        outputlist = []
        for tuple in input_tuples:
            len
        # sorted_tuples = sorted(tuples_list, key=lambda x: (x[0], int(x[1]), int(x[2])))
        
        # return sorted_tuples

    def main(self):

        input_tuples = self.get_input()
        sorted_tuples = self.sort_tuples(input_tuples)

        # print("Sorted tuples:")
        # for t in sorted_tuples:
        #     print(t)



object1 = Exercise2()
object1.main()
"""
Tom,19,80
 John,20,90
 Jony,17,91
 Jony,17,93
 Json,21,85
 """