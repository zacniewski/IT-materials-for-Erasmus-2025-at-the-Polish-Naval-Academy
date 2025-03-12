def min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return (min_value, max_value)

list_with_numbers = [3, 324, 4, 45, 2323, -2, -4, 324, 98, 232, 134, 13, 3]

my_min_value, my_max_value = min_max(list_with_numbers)

print("my_min_value = ", my_min_value)
print("my_max_value = ", my_max_value)
