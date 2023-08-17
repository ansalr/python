def intrest_rate():
    bank = []
    p = int(input())
    year = int (input())
    for i in range(2):
        sum = 0
        instalment = int(input())
        for j in range(instalment):
            year,mir = map(float,input().split())
            square_value = (1+mir)**(year*12)
            div = 1-1/square_value
            mult = p*mir
            emi = mult/div
            sum +=emi
        bank.append(sum)
    
    if bank[0]<bank[1]:
        return "Bank A"
    else:
        return "Bank B"
    
output = intrest_rate()
print(output)
