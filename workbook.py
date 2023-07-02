char = input()
def check(char):
    b= ["a"or"e"or"i"or"o"or"u"]
    if char in b:
        return "Vowel"
    else:
        return "Consonant"
a = check(char)
print(a)