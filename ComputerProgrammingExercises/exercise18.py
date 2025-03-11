numbers = [23, 5, 8, 45, 99, 1, 3, 56, 9, 80]

print("Sorted numbers with sorted() function: ", sorted(numbers))
print("Numbers looks like this: ", numbers)

print("Sorted numbers with sort() function: ", numbers.sort())
print("Numbers looks like this: ", numbers)

print("Sorted numbers with sort() function (reversed): ", numbers.sort(reverse=True))
print("Numbers looks like this: ", numbers)

for i in numbers:
    print(i)
