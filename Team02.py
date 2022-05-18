# Calvin Bullock
# April 25th, 2021

first = input("First name: ").capitalize()
last = input("Last name: ").upper()
email = input("Email address: ")
phone_num = input("Phone number: ")
job_title =input("Job title: ").title()
id_num = input("ID Number: ")

hair_color = input("Hair color: ").capitalize()
eye_color = input("Eyes color: ").capitalize()
start_month = input("Start month: ").capitalize()
training = input("Training yes/No: ").capitalize()

print("\nThe ID Card is:")
print("----------------------------------------")
print("{1}, {0}".format(first, last))
print(job_title)
print("ID: {0}\n".format(id_num))

print(email)
print(phone_num)
print()
print("Hair: {0:15} Eyes: {1}".format(hair_color, eye_color))
print("Month: {0:14} Training: {1}".format(start_month, training))
print("----------------------------------------")

# TODO this is an exsample of what it should iutput and input

# Please enter the following information:

# First name: Jane
# Last name: Doe
# Email address: JaneDoe@email.com
# Phone number: (208) 555-1234
# Job title: chief software architect
# ID Number: 83-23821

# The ID Card is:
# ----------------------------------------
# DOE, Jane
# Chief Software Architect
# ID: 83-23821

# janedoe@email.com
# (208) 555-1234

# Hair: Brown           Eyes: Blue
# Month: September      Training: Yes
# ----------------------------------------