first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

first_number = float(first_number)
second_number = float(second_number)

difference = abs(first_number - second_number)
if difference == int(difference):
    print(f"The difference between {first_number} and {second_number} is an integer? True!")
else:
    print(f"The difference between {first_number} and {second_number} is an integer? False!")