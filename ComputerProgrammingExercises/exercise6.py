x = input("Please, type your first number: ")
y = input("Please, type your second number: ")

integer_x = int(x)
integer_y = int(y)

if integer_x > integer_y:
    print("x is greater than y")
elif integer_x == integer_y:
    print("Both values are equal!")
else:
    print("y is greater than x")
