def min_starting_value(array):
    prefix_sum = 0
    min_x = 0

    for num in array:
        prefix_sum += num
        min_x = min(min_x, prefix_sum)
    if min_x < 0 :
        return 1 - min_x
    else:
        return 1


array = [-4,3,2,1]
result = min_starting_value(array)
print(result)
