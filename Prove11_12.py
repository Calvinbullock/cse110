
intrest_year = int(input("Enter the year of interest: "))

average_life_ex = 0
average_count = 0

min_life_exp = 100.0
min_life_country = 0
min_life_year = 0

max_life_exp = 0.00
max_life_country = 0
max_life_year = 0

intrest_min_life_exp = 100.0
intrest_min_life_country = 0

intrest_max_life_exp = 0.00
intrest_max_life_country = 0

with open("life-expectancy.csv") as life_file:
    next(life_file)
    for line in life_file:

        country, country_code, year, life_expectancy = line.strip().split(",")
        year = int(year)
        life_expectancy = float(life_expectancy)

        if min_life_exp > life_expectancy:
            min_life_exp = life_expectancy
            min_life_country = country
            min_life_year = year

        if max_life_exp < life_expectancy:
            max_life_exp = life_expectancy
            max_life_country = country
            max_life_year = year
        
        if year == intrest_year:
            average_life_ex += life_expectancy
            average_count += 1

            if intrest_min_life_exp > life_expectancy:
                intrest_min_life_exp = life_expectancy
                intrest_min_life_country = country

            if intrest_max_life_exp < life_expectancy:
                intrest_max_life_exp = life_expectancy
                intrest_max_life_country = country
            
    average_life_ex = average_life_ex / average_count

print()
print(f"The overall max life expectancy is: {max_life_exp} from {max_life_country} in {max_life_year}")
print(f"The overall min life expectancy is: {min_life_exp} from {min_life_country} in {min_life_year}")

print()
print(f"For the year {intrest_year}")
print(f"The average life expectancy across all countries was {average_life_ex:.2f}")
print(f"The max life expectancy was in {intrest_max_life_country} with {intrest_max_life_exp}")
print(f"The min life expectancy was in {intrest_min_life_country} with {intrest_min_life_exp}")


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

