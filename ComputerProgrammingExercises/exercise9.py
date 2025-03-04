import math

def calculate_surface_of_circle(radius):
    float_radius = float(radius)
    area = math.pi * float_radius ** 2
    return area


r = input("Please, type the radius: ")
print("The area of circle is: ", calculate_surface_of_circle(r))
