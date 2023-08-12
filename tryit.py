def sort_numbers_with_indices(numbers):
    sorted_indices = sorted(enumerate(numbers), key=lambda x: x[1])
    sorted_numbers = [x[1] for x in sorted_indices]
    original_indices = [x[0] for x in sorted_indices]
    return sorted_numbers, original_indices

# Sample input
numbers = [7, 3, 10, 5, 2]

# Sorting the numbers while keeping track of original indices
sorted_numbers, original_indices = sort_numbers_with_indices(numbers)

# Displaying the sorted numbers and original indices
for index, value in enumerate(sorted_numbers):
    original_index = original_indices[index]
    print(f"Number: {value}, Original Index: {original_index} ")
