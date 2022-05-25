

seconed_age = 100
seconed_height = 100

age = int(input("What is the age of the first rider? ")) #82
height = int(input("What is the height of the first rider? ")) #75

if age > 11 and age < 18:
    has_ticket = input("Does this rider have a golden passport (yes/no)? ")
    if  has_ticket == "yes":
        age = 18

second_rider = input("Is there a second rider (yes/no)? ").upper() #yes

if second_rider == "YES":
    seconed_age = int(input("What is the age of the second rider? ")) #14
    seconed_height = int(input("What is the height of the second rider? ")) #35

    if age > 11 and age < 18:
        has_ticket = input("Does this rider have a golden passport (yes/no)? ")
        if  has_ticket == "yes":
            age = 18

    if ((height >= 36) and (seconed_height >= 36)) and \
        (((age >= 18) or (seconed_age >= 18)) and \
        ((age >= 12) and (seconed_age >= 12))):
        print("Welcome to the ride. Please be safe and have fun!")
    elif (age >= 16 and seconed_age >= 14) or (seconed_age >= 16 and age >= 14):
        print("Welcome to the ride. Please be safe and have fun!")
    elif (age > 11 and height > 51) and (seconed_age > 11 and seconed_height > 51) :
        print("Welcome to the ride. Please be safe and have fun!")
    else:
        print("Sorry, you may not ride.")

elif age >= 18 and height >= 62:
    print("Welcome to the ride. Please be safe and have fun!")

else:
    print("Sorry, you may not ride.")
    
print()


# TODO rules
# No one under 36 inches may ever ride, either by themselves or with another rider.
# Normally, two riders sit in the car together. 
# A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
# If there are two riders and one of them is at least 18 years old, they may ride together.

# # TODO Streach ****
# If there are two riders, but neither one is at least 18 years old, 
# they may still ride as long as they are both at least 12 years old and at least 52 inches tall.

# If a person is age 12–17, ask if that person has a golden passport.
# If they do, they should be treated as if they were 18 years old for the sake of all rules.
# (Don't forget to apply this to the single rider case.)

# If there are two riders, but neither one is at least 18 years old,
# they may still ride if one rider is at least 16 years old and the other is at least 14.
# (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)

# TODO TestCase 1
# What is the age of the first rider? 82
# What is the height of the first rider? 75
# Is there a second rider (yes/no)? yes
# What is the age of the second rider? 14
# What is the height of the second rider? 35
# Sorry, you may not ride.

# TODO TestCase 2
# What is the age of the first rider? 82
# What is the height of the first rider? 75
# Is there a second rider (yes/no)? yes
# What is the age of the second rider? 14
# What is the height of the second rider? 36
# Welcome to the ride. Please be safe and have fun!

# TODO TestCase 3
# What is the age of the first rider? 12
# What is the height of the first rider? 46
# Is there a second rider (yes/no)? no
# Sorry, you may not ride.






# test stretch 1:

# What is the age of the first rider? 12

# What is the height of the first rider? 36

# Does this rider have a golden passport (yes/no)? no

# Is there a second rider (yes/no)? yes

# What is the age of the second rider? 12

# What is the height of the second rider? 38

# Does this rider have a golden passport (yes/no)? no

# Sorry, you may not ride.

 

# What is the age of the first rider? 12

# What is the height of the first rider? 54

# Does this rider have a golden passport (yes/no)? no

# Is there a second rider (yes/no)? yes

# What is the age of the second rider? 12

# What is the height of the second rider? 52

# Does this rider have a golden passport (yes/no)? no

# Welcome to the ride. Please be safe and have fun!

 

 

 

# test stretch 2:

# What is the age of the first rider? 18

# What is the height of the first rider? 52

# Is there a second rider (yes/no)? yes

# What is the age of the second rider? 12

# What is the height of the second rider? 52

# Does this rider have a golden passport (yes/no)? yes

# Welcome to the ride. Please be safe and have fun!

 

# What is the age of the first rider? 12

# What is the height of the first rider? 52

# Does this rider have a golden passport (yes/no)? yes

# Is there a second rider (yes/no)? no

# Sorry, you may not ride.

 

# What is the age of the first rider? 12

# What is the height of the first rider? 62

# Does this rider have a golden passport (yes/no)? yes

# Is there a second rider (yes/no)? no

# Welcome to the ride. Please be safe and have fun!

 

 

 

# test stretch 3:

# What is the age of the first rider? 14

# What is the height of the first rider? 36

# Does this rider have a golden passport (yes/no)? no

# Is there a second rider (yes/no)? yes

# What is the age of the second rider? 16

# What is the height of the second rider? 37

# Does this rider have a golden passport (yes/no)? no

# Welcome to the ride. Please be safe and have fun!

 

# What is the age of the first rider? 14

# What is the height of the first rider? 52

# Does this rider have a golden passport (yes/no)? no

# Is there a second rider (yes/no)? yes

# What is the age of the second rider? 16

# What is the height of the second rider? 35

# Does this rider have a golden passport (yes/no)? no

# Sorry, you may not ride.

 

# What is the age of the first rider? 15

# What is the height of the first rider? 36

# Does this rider have a golden passport (yes/no)? no

# Is there a second rider (yes/no)? yes

# What is the age of the second rider? 15

# What is the height of the second rider? 51

# Does this rider have a golden passport (yes/no)? no

# Sorry, you may not ride.