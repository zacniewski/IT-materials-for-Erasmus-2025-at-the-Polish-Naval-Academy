import math

def calculate_surface_of_circle(radius):
    return math.pi * radius ** 2

r = input("Please, type the radius: ")

float_radius = float(r)  # change type from string to float

area = calculate_surface_of_circle(float_radius)

print("The area of circle is:", area)
