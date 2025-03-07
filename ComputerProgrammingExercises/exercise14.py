t = ['spam', 2.0, 5, [10, 20]]
print("Type is: ", type(t))
print("Length is: ", len(t))

print("First value is: ", t[0])

# Lists are mutasble
t[0] = 'different value'
print("The list is now:", t)

# Check if 5 number is inside the 't' list
print(5 in t)

