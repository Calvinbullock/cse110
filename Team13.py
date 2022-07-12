from cmath import pi

def compute_rectangle_area(rec_length, rec_width):
    return rec_length * rec_width

# Base code modified for strech 0.3
def compute_square_area(sqr_length):
    return compute_rectangle_area(sqr_length, sqr_length)

def compute_cir_area(cir_radias):
    return cir_radias ** 2 * pi

def compute_area(shape, length, width = 0):
    if shape.lower() == "square":
        return compute_rectangle_area(length, length)

    elif shape.lower() == "circle":
        return compute_cir_area(length)

    elif shape.lower() == "rectangle":
        return compute_rectangle_area(length, width)
        

loop_again = True
while loop_again:

    shape = input("What shape would you like to compute? ")
    length = float(input(f"What is the length in cm? "))
    width = float(input(f"What is the width in cm? "))

    if shape.lower() == "rectangle": 
        print(f"The area of the {shape} is: {compute_area(shape, length, width):.2f} square centimeters.")
        loop_again = False
    
    elif shape.lower() == "square" or shape.lower() == "circle": 
        print(f"The area of the {shape} is: {compute_area(shape, length):.2f} square centimeters.")
        loop_again = False



    # if shape.lower() == "rectangle": 
    #     rec_length = float(input(f"What is the length of rectangle in cm? "))
    #     rec_width = float(input(f"What is the width of the rectanglein cm? "))
    #     print(f"The area of the rectangle is: {compute_rectangle_area(rec_length, rec_width):.2f} square centimeters.")
    #     loop_again = False

    # elif shape.lower() == "square":
    #     sqr_length = float(input("What is the length of a side of the square in cm? "))
    #     print(f"The area of the square is: {compute_square_area(sqr_length):.2f} square centimeters.")
    #     loop_again = False

    # elif shape.lower() == "circle":
    #     cir_radias = float(input("What is the radius of the circle in cm? "))
    #     print(f"The area of the rectangle is: {compute_cir_area(cir_radias):.2f} square centimeters.")
    #     loop_again = False

