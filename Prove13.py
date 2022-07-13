
temp = float(input("What is the temperature? "))
units = input("Fahrenheit or Celsius (F/C)? ").upper()
wind_speed = 5

def wind_chill(temp, V):
    return 35.74 + 0.6215 * temp - 35.75 * (V ** 0.16) + 0.4275 * temp * (V ** 0.16)

def unit_converstion_to_f(c_temp):
     return (c_temp * 9/5) + 32

# converts the Celsius temp to input as a Fahrenheit
if units == "C":
    temp = unit_converstion_to_f(temp)

while wind_speed < 61:
    wind_chill_num = wind_chill(temp, wind_speed)

    print(f"At temperature {temp}, and wind speed {wind_speed} mph, the windchill is: {wind_chill_num:.2f}F")
    wind_speed += 5



# T is the temperature in degrees Fahrenheit
# V is the wind speed in miles per hour
# V^0.16 means V to the power of 0.16, which can be found in Python using the ** operator.

# What is the temperature? 8
# Fahrenheit or Celsius (F/C)? F
# At temperature 8.0F, and wind speed 5 mph, the windchill is: -1.11F
# At temperature 8.0F, and wind speed 10 mph, the windchill is: -6.02F
# At temperature 8.0F, and wind speed 15 mph, the windchill is: -9.15F
# At temperature 8.0F, and wind speed 20 mph, the windchill is: -11.50F
# At temperature 8.0F, and wind speed 25 mph, the windchill is: -13.40F
# At temperature 8.0F, and wind speed 30 mph, the windchill is: -15.00F
# At temperature 8.0F, and wind speed 35 mph, the windchill is: -16.39F
# At temperature 8.0F, and wind speed 40 mph, the windchill is: -17.62F
# At temperature 8.0F, and wind speed 45 mph, the windchill is: -18.73F
# At temperature 8.0F, and wind speed 50 mph, the windchill is: -19.74F
# At temperature 8.0F, and wind speed 55 mph, the windchill is: -20.67F
# At temperature 8.0F, and wind speed 60 mph, the windchill is: -21.53F

# What is the temperature? -10
# Fahrenheit or Celsius (F/C)? C
# At temperature 14.0F, and wind speed 5 mph, the windchill is: 5.93F
# At temperature 14.0F, and wind speed 10 mph, the windchill is: 1.42F
# At temperature 14.0F, and wind speed 15 mph, the windchill is: -1.47F
# At temperature 14.0F, and wind speed 20 mph, the windchill is: -3.63F
# At temperature 14.0F, and wind speed 25 mph, the windchill is: -5.38F
# At temperature 14.0F, and wind speed 30 mph, the windchill is: -6.85F
# At temperature 14.0F, and wind speed 35 mph, the windchill is: -8.13F
# At temperature 14.0F, and wind speed 40 mph, the windchill is: -9.27F
# At temperature 14.0F, and wind speed 45 mph, the windchill is: -10.29F
# At temperature 14.0F, and wind speed 50 mph, the windchill is: -11.22F
# At temperature 14.0F, and wind speed 55 mph, the windchill is: -12.07F
# At temperature 14.0F, and wind speed 60 mph, the windchill is: -12.87F