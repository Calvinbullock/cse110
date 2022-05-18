# Autor Calvin Bullock
# Date: 3rd of May 2022

from cmath import pi

# Bsse code modified for strech 0.3
sqr_length = float(input("What is the length of a side of the square in cm? "))
sqr_area = sqr_length * sqr_length
print(f"The area of the square is: {sqr_area} square centimeters.\n")
print(f"The area of the square is: {sqr_area/10000} square meters.\n")

rec_length = float(input(f"What is the length of rectangle in cm? "))
rec_width = float(input(f"What is the width of the rectanglein cm? "))
rec_area = rec_length * rec_width
print(f"The area of the rectangle is: {rec_area} square centimeters.\n")
print(f"The area of the rectangle is: {rec_area/10000} square meters.\n")

cir_radias = float(input("What is the radius of the circle in cm? "))
cir_area = cir_radias ** 2 * pi
print(f"The area of the circle is: {cir_area} square centimeters.")
print(f"The area of the circle is: {cir_area/10000} square meters.")


# strach 0.2 CODE
length = float(input("Please input a length: "))
sqr_area = length * length 
cir_area = cir_area = length ** 2 * pi
cube_vol = length ** 3
sphere_vol = 4/3 * pi * length ** 3

print(f"The area for the square is: {sqr_area}.")
print(f"The area for the circle is: {cir_area}.")
print(f"The volume for the cube is: {cube_vol}.")
print(f"The volume for the sphere is: {sphere_vol}.")


# TODO strech 0.3
# For each of the three areas in the core requirements,
# change the prompt for the user to ask for the value in centimeters.
# Then, display the resulting area in both square centimeters and square meters.
# Keep in mind that a centimeter is 1/100 of a meter,
# and a square centimeter is 1/10,000 of a square meter.

# TODO strech 0.2
# areas of a square with that length of side, 
# a circle with that radius, 
# and then the volumes of a cube with that side 
# and a sphere with that radius, 
# all from the same value from the user.


# TODO exsample 1 
# What is the length of a side of the square? 5
# The area of the square is: 25.0
# What is the length of rectangle? 6
# What is the width of the rectangle? 7
# The area of the rectangle is: 42.0
# What is the radius of the circle? 5
# The area of the circle is: 78.5

# TODO exsample 2
# What is the length of a side of the square? 3.5
# The area of the square is: 12.25
# What is the length of rectangle? 6
# What is the width of the rectangle? 7.5
# The area of the rectangle is: 45.0
# What is the radius of the circle? 8.2
# The area of the circle is: 211.1336
