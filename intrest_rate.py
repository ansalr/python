p = int(input())
year = int (input())
sum = 0
instalment = int(input())
year,mir = map(float,input().split())
square_value = (1+mir)**(year*12)
div = 1-1/square_value
mult = p*mir
emi = mult/div
print(emi)