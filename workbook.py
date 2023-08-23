arr = [345,604,321,433,704,470,808,718,517,811]
empty = []

for i in range(2):
        count = 0  
        len_arr,r_range = map(int,input().split())
        for val in arr:
            
            if (val>=len_arr and val<=r_range):
                        count+=1
        empty.append(count)

print(empty)