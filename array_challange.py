def ArrayChallenge(strArr):
    cache = []
    for char in strArr:
        if char not in cache:
            if len(cache) == 5:
                cache.pop()
            cache.insert(0, char)
        else:
            cache.remove(char)
            cache.insert(0, char)
    return '-'.join(cache)


input_array = ["A", "B", "C", "D", "A", "E", "D", "Z"]
result = ArrayChallenge(input_array)
def revers(string):
    revers_str =''
    index = len(string)
    while index:
        index-=1
        revers_str +=string[index]
    return revers_str

 
answer = revers(result)
print(answer)


# Output: "C-A-E-D-Z"
