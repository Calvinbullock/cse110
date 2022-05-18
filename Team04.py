import math

print("Welcome to the velocity calculator. Please enter the following: ")

mass = float(input("Mass (in kg): ")) #5
area = float(input("Cross sectional area (in m^2): ")) #0.01
drag = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): ")) #0.5

gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): ")) #9.8
fluid_density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): ")) #1.3
time = float(input("Time (in seconds): ")) #10


# area = (math.pi * area ** 2)

# hard code for faster testing
# mass = float(5)
# area = float(0.01)
# drag = float(0.5)

# gravity = float(9.8)
# fluid_density = float(1.3)
# time = float(10)

e = 2.71828 # This is a physical constant, I think.
c = (1/2) * fluid_density * area * drag # I dont know what this c stands for....

# Broke up the equation to make it cleaner and easyer to read.
sqrt = math.sqrt(mass * gravity * c)
power = (-(sqrt / mass) * time)
velocity_at_t = round(math.sqrt((mass * gravity) / c) * (1 - e ** power), 3)

print(f"\nThe inner value of c is: {round(c, 3)}") #0.003
print(f"The velocity after 10.0 seconds is: {velocity_at_t} m/s") #67.512 m/s


# Bowling ball
# 8 cm Radia
# 2.85 kg
# 0.5 Drag coeficent 