number = input()
rev_num = str(number)[::-1]
if type(number)==int:
    print(int(rev_num))
elif type(number)==float:
    print(int(rev_num)) 
else:
    print(rev_num)