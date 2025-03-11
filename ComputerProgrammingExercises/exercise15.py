letters = ['a', 'b', 'c', 'd']
# print(letters[-1])
# print(type(letters[0]))
# print(letters + letters)

numbers = [2, 4, 6, 45, 67, 67, 2332, 3323, 8989, 3232, 323, 34.9]

print("Sum of all numbers is: ", sum(numbers))
print("Minimum of all numbers is: ", min(numbers))
print("Maximum of all numbers is: ", max(numbers))

# Adding values to the list
numbers.append(1000)
numbers.append(444)
numbers.append(777)
print("The numbers are now: ", numbers)

numbers.extend([123, 456])
print("The numbers are now: ", numbers)

numbers.insert(2, 'three')

# Removing values from the list
print("Length of 'numbers' list is: ", len(numbers))
print("The numbers are now: ", numbers)

# 'pop' needs an index of data
numbers.pop(6)
print("The numbers are now: ", numbers)

# 'remove' needs a value
numbers.remove(67)
print("The numbers are now: ", numbers)
