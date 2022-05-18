
#TODO Complete
# This is the lv 3 part 1 of 6
def lv_three_1_of_6():
    l = 1 # LV 3
    while l == 1:
        choice = input("Nar:\tDo you TLAK to it, fight it, or RUN?\n").upper()
        if choice == "TALK":
            l = 0
            print("Nar:\tYou kneel in front of the dragon and ask that he not eat you.")
            print("Nar:\tThe dragon replies, he eats you.")
            print("Nar:\tGAME OVER")
            
            # TODO finish the story here##### AGREE or DIE
        elif choice == "RUN":
            l = 0
            print("Nar:\tYou take off again. The dragon jumps at you and carrys you into the sky.")
            print("Drag:\t\" I win!\" the dragon says with a chuckle.")
            print("You:\t\"What is going on are you going to eat me?\"")
            print("Drag:\t\"No not me, my children.\nIf you had deminstarted you abillity to best me I may have spared your life, but the hunt is over..\"")
            print("Nar:\tGAME OVER")
        
        elif choice == "FIGHT":
            l = 0
            print("Nar:\tYou pick up a stick and take a deffensive stance.")
            print("Drag:\t\"You have never beat me before, but go ahead and try again.\" He says as he falls over laughing.")
            print("You:\tYou look at it confused. \"You mean your not going to eat me?\"")
            print("Drag:\t\"If you win no.\" He growls.")
            print("Nat:\tYou charge him and he eats you.")
            print("Nar:\tGAME OVER")
            
        else:
            print("Error:\t input not recognized, try agian.")
    # While Lv3 - 1/6

# TODO 
# This is the lv 3 part 2 of 6
def lv_three_2_of_6():
    l = 1 # LV 3
    while l == 1:
        choice = input("Nar:\tDo you KILL it or take it HOSTAGE \n").upper()
        if choice == "KILL":
            l = 0
            print("Nar:\tYou start looking for a weapon but the biger dragon crawls his way in.")
            print("Nar:\tHe sees you in here and eats out of fear of you harming the baby.")
            print("Nar:\tGAME OVER")
            
        elif choice == "HOSTAGE":
            l = 2
            print("Nar:\tYou wait quietly for the dragon to come back, you hear him come into the bigger room of the cave.")
            print("You:\t\"If you come in here I will hurt the baby.\"")
            print("Drag:\tYou if you hurt him I will kill you, but if you come out now I will let you go free.")
            print("Nar:\tYou agree and the dragon leaves lets you leave with a promise to no longer hunt you.")
            print("Nar:\tGAME OVER, YOU WIN")
            
        else:
            print("Error:\t input not recognized, try agian.")
    # while Lv 3 - 2/6

# This is the lv 2 part 1 of 4 -- This function calls lv 3 parts 1 - 2
def lv_two_1_of_4():
    k = 1 # LV 2
    while k == 1:
        choice = input("Nar:\tDo you, EXIT the cave or GO further in?\n").upper()
        if choice == "EXIT":
            print("Nar:\tYou exit the cave and the dragon drops down right in front of you.")
            k = 0
            lv_three_1_of_6()
            
        elif choice == "GO":
            print("Nar:\tYou walk further in and start feeling along the wall until you see the cave open up, there is a light!")
            print("Nar:\tYou look up and see a light up at the top of the cave, its an opening to the sky.")
            print("Nar:\tYou look around and see another tunnel and hear cries comeing from it, you follow them.")
            print("Nar:\tYou find a baby dragon inside.")
            k = 0
            lv_three_2_of_6()
            
        else:
            print("Error:\t input not recognized, try agian.")
    # While Lv 2 - 1/2

#
def lv_three_3_of_6():
    l = 1 # LV 3
    while l == 1:
        choice = input("You look at a tree and wounder if you should CLIMB it or keep RUNNING")
        if choice == "CLIMB":
            print("You climb the tree and as you get to the top ")
            l = 0
        elif choice == "RUNNING":
            print("")
            l = 0
        else:
            print("Error:\t input not recognized, try agian.")
    # While Lv 3 - 3/6

# TODO not done ---
def lv_three_4_of_6():
    l = 1 # LV 3    
    while l == 1:
        choice = 1
        

# This is the lv 2 part 2 of 4 -- This function calls lv 3 parts 3 - 4
def lv_two_2_of_4():
    k = 1 # LV 2
    while k == 1:
        choice = input("Do you choose to turn BACK to the forest or get on the BOAT?\n").upper()
        if choice == "BACK":
            k = 0
            print("You turn around and run back into the woods.")
            lv_three_3_of_6()
            
        elif choice == "BOAT":
            k = 0
            lv_three_4_of_6()
            
        else:
            print("Error:\t input not recognized, try agian.")
    # While Lv 2 - 2/2

# This is the lv 1 part 1 of 2 ** This function calls lv 2 parts 1 - 2
def lv_one_1_of_2():
    j = 1 # LV 1
    while j == 1:   
        choice = input("Do you keep RUNING or ENTER.\n").upper()
        if choice == "ENTER":
            print("Nar:\tYou enter the cave and take shelter in there.")
            print("Nar:\tYou step on something and hear a crack.\nYou reach down and feel a broken bone.")
            j = 0
            lv_two_1_of_4()
            
        elif choice == "RUNNING":
            print("You turn to run off into the forest.")
            print("You see that the woods are starting to thin out, you stop at the edge of ocean and see a small motoer boat on the beach.")
            j = 0
            lv_two_2_of_4()
            
        else:
            print("Error:\t input not recognized, try agian.")
    # While Lv 1 - 1

# Main function
def game_start():
    print("Nar:\tYou wake up you look up at the cliff lay laying under,\nthe last thing you can remember is being chased by a dragon.")
    print("Nar:\tYou hear a roar from the sky.")

    # variables for the loops to repet the if until a valid answer is entered.
    i = 1 # LV 0
    j = 1 # LV 1
    k = 1 # LV 2
    l = 1 # LV 3

    # choice branch 1 
    while i == 1:
        print("Nar:\tYou start scaning the sky and see the dragon diveing toward you,")
        choice = input("what do you do? RUN or HIDE.\n").upper()

        if choice == "RUN":
            print("Nar:\tYou take off into the woods.")
            print("Nar:\tYou come up to a cave, it smells terable and is dark.")
            i = 0
            lv_one_1_of_2()

        elif choice == "HIDE": # TODO base one -- -- -- -- - - - - -------------------------------------------------------------------- ###
            print("Nar:\tYou jump into a bush.")


            i = 0
        else:
            print("Error:\t input not recognized, try agian.")

# This is the main function sorta
game_start()
