def sort_tuples(tuples):
    def compare(t1, t2):
        if t1[3] != t2[3]:
            return 1 if t1[3] > t2[3] else -1
        elif t1[0] != t2[0]:
            return 1 if t1[0] > t2[0] else -1
        elif t1[1] != t2[1]:
            return 1 if t1[1] > t2[1] else -1
        elif t1[2] != t2[2]:
            return 1 if t1[2] > t2[2] else -1
        else:
            return 0

    n = len(tuples)
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare(tuples[j], tuples[j + 1]) > 0:
                tuples[j], tuples[j + 1] = tuples[j + 1], tuples[j]

    return tuples

tuples = [('Reny', 19, 80, 'F'), ('John', 20, 90, 'M'), ('Jony', 17, 91, 'M'), ('Jony', 17, 93, 'M'), ('Reny', 28, 85, 'F'), ('Jason', 21, 85, 'F'), ('Angel', 19, 79, 'F')]
sorted_tuples = sort_tuples(tuples)
print(sorted_tuples)

