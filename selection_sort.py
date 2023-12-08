arr = [4,5,2,3,1]


for j in range(len(arr)-1):
    min = j
    for i in range(j+1,len(arr)):
        if arr[i] < arr[min] :
            min = i
    
    arr[min],arr[j] = arr[j],arr[min]
                
    

print(arr)