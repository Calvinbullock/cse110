
grade_num = int(input("Please enter a grade persentage: "))
seconed_digit = grade_num % 10

# changes grade % to a letter
if grade_num >= 90:
    letter = "A"
elif grade_num >= 80:
    letter = "B"
elif grade_num >= 70:
    letter = "C"
elif grade_num >= 60:
    letter = "D"
elif grade_num < 60:
    letter = "F"

# checks if you are a + or - student
if grade_num >= 90 or grade_num < 60:
    pass
elif seconed_digit >= 7:
    letter = letter + "+"
else:
    letter = letter + "-"

# checks if you pass or fail, pass is grater then 70% 
if grade_num >= 70:
    print("You passed! Great job.")
else:
    print("You Failed, try again you can do it!")

print(f"your letter grade is: {letter}")