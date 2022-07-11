
def wind_chill(T, V):
    return 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)

def unit_converstion(celsius):
     return celsius * (9/5) + 32

temp = float(input("What is the temperature? "))
units = input("Fahrenheit or Celsius (F/C)? ").upper()

speed = 5 

while speed < 61:
    wind_chill_num = wind_chill(temp, speed)
    
    if units == "C":
        wind_chill_num = unit_converstion(wind_chill_num)

    print(f"At temperature 8.0F, and wind speed {speed} mph, the windchill is: {wind_chill_num:.2f}{units}")
    speed += 5



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