
choice = int(input("Would you like to input a 1.year or a 2.country? ")) 

if choice == 1:
    spec_yr = int(input("Enter the year of interest: "))
    spec_ctry = "null"

elif choice == 2:
    spec_ctry = input("Enter the country of interest: ")
    spec_yr = -100
    
spec_min_life_exp = 100.0
spec_min_life_ctry = 0
spec_max_life_exp = 0.00
spec_max_life_ctry = 0

avg_life_ex = 0
avg_count = 0

min_life_exp = 100.0
min_life_country = 0
min_life_yr = 0

max_life_exp = 0.00
max_life_country = 0
max_life_yr = 0

with open("life-expectancy.csv") as life_file:
    next(life_file)
    for line in life_file:

        country, country_code, year, life_expectancy = line.strip().split(",")
        year = int(year)
        life_expectancy = float(life_expectancy)

        # finds the country and year with the smallest life expectancy in the whole data set
        if min_life_exp > life_expectancy:
            min_life_exp = life_expectancy
            min_life_country = country
            min_life_yr = year

         # finds the country and year with the greatest life expectancy in the whole data set
        if max_life_exp < life_expectancy:
            max_life_exp = life_expectancy
            max_life_country = country
            max_life_yr = year

        # Finds the greatest and least life expectancy with a matching year or country to user input
        if year == spec_yr or country.lower() == spec_ctry.lower():
            avg_life_ex += life_expectancy
            avg_count += 1

            if spec_min_life_exp > life_expectancy:
                spec_min_life_exp = life_expectancy
                spec_min_life_ctry = country

            if spec_max_life_exp < life_expectancy:
                spec_max_life_exp = life_expectancy
                spec_max_life_ctry = country

            
    avg_life_ex = avg_life_ex / avg_count

print()
print(f"The overall max life expectancy is: {max_life_exp} from {max_life_country} in {max_life_yr}")
print(f"The overall min life expectancy is: {min_life_exp} from {min_life_country} in {min_life_yr}")

print()
if choice == 1:
    print(f"For the year {spec_yr}")
    print(f"The average life expectancy across all countries was {avg_life_ex:.2f}")
    print(f"The max life expectancy was in {spec_max_life_ctry} with {spec_max_life_exp}")
    print(f"The min life expectancy was in {spec_min_life_ctry} with {spec_min_life_exp}")

elif choice == 2:
    print(f"For the country {spec_ctry}")
    print(f"The average life expectancy across all countries was {avg_life_ex:.2f}")
    print(f"The max life expectancy in {spec_max_life_ctry} was {spec_max_life_exp}")
    print(f"The min life expectancy in {spec_min_life_ctry} was {spec_min_life_exp}")



# TODO INFO
# What is the year and country that has the lowest life expectancy in the dataset?

# What is the year and country that has the highest life expectancy in the dataset?

# Allow the user to type in a year, then, find the average life expectancy for that year.
# Then find the country with the minimum and the one with the maximum life expectancies for that year.

# TODO exsample
# Enter the year of interest: 1959

# The overall max life expectancy is: 86.751 from Monaco in 2019
# The overall min life expectancy is: 17.76 from Iceland in 1882

# For the year 1959:
# The average life expectancy across all countries was 54.95
# The max life expectancy was in Norway with 73.49
# The min life expectancy was in Mali with 28.077

