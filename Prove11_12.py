
choice = int(input("Would you like to input a 1.year or a 2.country? ")) 

if choice == 1:
    spec_yr = int(input("Enter the year of interest: "))

    spec_yr_min_life_exp = 100.0
    spec_yr_min_life_ctry = 0
    spec_yr_max_life_exp = 0.00
    spec_yr_max_life_ctry = 0

elif choice == 2:
    spec_ctry = int(input("Enter the country of interest: "))


average_life_ex = 0
average_count = 0

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

        if choice == 1:
            # Finds the greatest and least life expectancy with a matching year to user input
            if year == spec_yr:
                average_life_ex += life_expectancy
                average_count += 1

                if intrest_min_life_exp > life_expectancy:
                    spec_yr_min_life_exp = life_expectancy
                    spec_yr_min_life_ctry = country

                if intrest_max_life_exp < life_expectancy:
                    spec_yr_max_life_exp = life_expectancy
                    spec_yr_max_life_ctry = country

        else:
            # Finds the greatest and least life expectancy with a matching country to user input
            if year == spec_ctry:
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
print(f"The overall max life expectancy is: {max_life_exp} from {max_life_country} in {max_life_yr}")
print(f"The overall min life expectancy is: {min_life_exp} from {min_life_country} in {min_life_yr}")

print()
print(f"For the year {spec_yr}")
print(f"The average life expectancy across all countries was {average_life_ex:.2f}")
print(f"The max life expectancy was in {spec_yr_max_life_ctry} with {spec_yr_max_life_exp}")
print(f"The min life expectancy was in {spec_yr_min_life_ctry} with {spec_yr_min_life_exp}")


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

