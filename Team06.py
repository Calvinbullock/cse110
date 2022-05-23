

seconed_age = 100
seconed_height = 100

age = int(input("What is the age of the first rider? ")) #82
height = int(input("What is the height of the first rider?")) #75
second_rider = input("Is there a second rider (yes/no)? ").upper() #yes

if second_rider == "YES":
    seconed_age = int(input("What is the age of the second rider? ")) #14
    seconed_height = int(input("What is the height of the second rider? ")) #35

    if height < 36:
        print("Sorry, you may not ride.")
    else:
        pass

elif age > 18 and height >= 62:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")


# single rider
if height < 36 or seconed_height < 36:
    print("Sorry, you may not ride.")
else:
    if age < 18 and second_rider < 18:
        print("Welcome to the ride. Please be safe and have fun!")


# What is the age of the first rider? 82
# What is the height of the first rider? 75
# Is there a second rider (yes/no)? yes
# What is the age of the second rider? 14
# What is the height of the second rider? 35
# Sorry, you may not ride.


# No one under 36 inches may ever ride, either by themselves or with another rider.

# Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.

# If there are two riders and one of them is at least 18 years old, they may ride together.