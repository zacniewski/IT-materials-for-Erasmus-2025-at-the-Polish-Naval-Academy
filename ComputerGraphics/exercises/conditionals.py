first = int(input("Type first number: "))
second = input("Type second number: ")
second = int(second)
third = int(input("Type third number: "))

if first > second:
    print("First number is greater than second number")
elif first == second:
    print("First number is equal to second number")
else:
    print("Second number is greater than first number")


if first > second & first > third:
    print("First number is the biggest of all numbers")
elif second > first and second > third:
    print("Second number is the biggest of all numbers")
elif first == second | first == third:
    print("Some numbers are equal")
else:
    print("Third number is the biggest of all numbers")