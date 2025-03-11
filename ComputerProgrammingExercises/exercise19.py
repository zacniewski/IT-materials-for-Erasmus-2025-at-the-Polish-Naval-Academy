my_dictionary = {1: 234, 3: 678, 'abc': 567}
print(type(my_dictionary))
print("My dictionary: ", my_dictionary)

my_dictionary[4] = "hello"
print("My dictionary (update 1): ", my_dictionary)
my_dictionary[3] = 4_754_754_875
my_dictionary[34.5] = "Today is not a sunny day"
print("My dictionary (update 2): ", my_dictionary)

my_dictionary[[1, 2, 3]] = 678

