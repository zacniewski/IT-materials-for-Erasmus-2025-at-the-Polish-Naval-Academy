a = input("Type length of the first side: ")
b = input("Type length of the second side: ")
c = input("Type length of the third side: ")

# Change the string values to float values
side_a = float(a)
side_b = float(b)
side_c = float(c)


# the result should be True or False
def is_right_triangle(s1, s2, s3):
    return s1**2 + s2**2 == s3**2


right_triangle = is_right_triangle(side_a, side_b, side_c)
print("Our triangle is right-angled: ", right_triangle)