def collecting_candies(t,num,arr):
    
    count = []
    a=arr[0]+arr[1]
    count.append(a)
    for i in range(2,len(arr)):
        a+=arr[i]
        count.append(a)        
    return sum(count)

    
    pass


t = int(input())
num = int(input())
arr = list(map(int,input().split()))
output = collecting_candies(t,num,arr)
print(collecting_candies(t,num,arr))