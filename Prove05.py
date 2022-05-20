
#TODO Complete
# This is lv 3 part 1 of 6
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
            print("ERROR:\t input not recognized, try agian.")

# TODO Complete
# This is lv 3 part 2 of 6
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
            print("ERROR:\t input not recognized, try agian.")

# TODO complete
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
            print("ERROR:\t input not recognized, try agian.")

# TODO Complete
# This is Lv 3 part 3 of 6
def lv_three_3_of_6():
    l = 1 # LV 3
    print("Nar:\tYou stop and think, if you climb a tree you could mabey see somewere to hide,\nor just make it easyer for the dragon to find you.")
    while l == 1:
        choice = input("Nar:\tYou stop and think if you CLIMB a tree it or keep RUNNING")
        if choice == "CLIMB":
            print("Nar:\tYou climb the tree and as you get to the top you look around and see a small town.")
            print("Nar:\tYou run to the town and when you arive you exsplane about the dragon and they take you in.")
            print("Nar:\tGAME OVER, YOU WIN")
            l = 0
        elif choice == "RUNNING":
            print("Nar:\tYou decide to keep running. You hear the sound of the dragon overhead. You keep running.")
            print("Nar:\tBut the dragon can hear you smashing through the brush in fear. He dives and grabs you with his teach.")
            print("Nar:\tGAME OVER, YOU LOSE")
            print("")
            l = 0
        else:
            print("ERROR:\t Input not recognized, try agian.")

# TODO Complete
# This is Lv 3 part 4 of 6
def lv_three_4_of_6():
    l = 1 # LV 3    
    while l == 1:
        choice = input("Nar:\tDo you choose to go to the ISLAND or cuntinue out to SEA?\n").upper()
        if choice == "ISLAND":
            k = 0
            print("Nar:\tYou reach the island and find a nice abandednd house that is still in very good repear.")
            print("and stocked with suplies. You decide to rest here as the ragon shouldn't know were you are.")
            print("Nar:\tGAME OVER, YOU WIN")
            
        elif choice == "SEA":
            k = 0
            print("Nar:\tYou keep heading out to sea and a strom rolls in, the little boat is no match for the waves.")
            print("It capsized and you meet a water grave.")
            print("Nar:\tGAME OVER, YOU LOSE")
            
        else:
            print("ERROR:\t Input not recognized, try agian.")

# TODO Complete
# This is the lv 2 part 2 of 4 -- This function calls lv 3 parts 3 - 4
def lv_two_2_of_4():
    k = 1 # LV 2
    while k == 1:
        choice = input("Nar:\tDo you choose to turn BACK to the forest or get on the BOAT?\n").upper()
        if choice == "BACK":
            k = 0
            print("You turn around and run back into the woods.")
            lv_three_3_of_6()
            
        elif choice == "BOAT":
            k = 0
            print("Nar:\tYou hop in the boat and start the moter the boat starts up and you gun the engion.")
            print("The boat starts skiming along the water and you see the forest you came from start to drop away in the distance.")
            print("ahead of you you see an island come into view.")
            lv_three_4_of_6()
            
        else:
            print("ERROR:\t Input not recognized, try agian.")

# TODO Complete
# This is the lv 1 part 1 of 2 ** This function calls lv 2 parts 1 - 2
def lv_one_1_of_2():
    j = 1 # LV 1
    while j == 1:   
        choice = input("Do you keep RUNING or ENTER.\n").upper()
        if choice == "ENTER":
            print("Nar:\tYou enter the cave and take shelter in it.")
            print("Nar:\tYou step on something and hear a crack.\nYou reach down and feel a bone on the ground.")
            j = 0
            lv_two_1_of_4()
            
        elif choice == "RUNNING":
            print("You turn to run off into the forest.")
            print("You see that the woods are starting to thin out, you stop at the edge of ocean and see a small motoer boat on the beach.")
            j = 0
            lv_two_2_of_4()
            
        else:
            print("ERROR:\t input not recognized, try agian.")

# TODO In progress
# This is the lv 1 part 2 of 2 ** This function calls lv 2 parts 1 - 2
def lv_one_2_of_2():
    print("Nar:\tYou try to be as quite as possible in the bush.")
    print("Nar:\tThe dragon slams into the ground and looks around.")
    print("Nar:\tHis eyes scaning the brush.")
    choice = input("What do you do? STAY or DISTRACT by throwing a rock?.\n").upper()
    if choice == "STAY":
        print("Nar:\tto be cuntinued")
    
    elif choice == "DISTRACT":
        print("Nar:\tto be cuntinued")
    
    else:
        print("ERROR:\tInput not recognized, try agian.")
        lv_one_2_of_2()

# TODO Use recurstion for the new fuctions
# # Main function
def game_start():
    print("Nar:\tYou wake up you look up at the cliff lay laying under,\nthe last thing you can remember is being chased by a dragon.")
    print("Nar:\tYou hear a roar from the sky.")

    i = 1 # LV 0
    # choice branch 1 
    while i == 1:
        print("Nar:\tYou start scaning the sky and see the dragon diveing toward you,")
        choice = input("What do you do? RUN or HIDE.\n").upper()

        if choice == "RUN":
            print("Nar:\tYou take off into the woods.")
            print("Nar:\tYou come up to a cave, it smells terable and is dark.")
            i = 0
            lv_one_1_of_2()

        elif choice == "HIDE":
            print("Nar:\tYou jump into a bush.")
            lv_one_2_of_2()
            i = 0

        else:
            print("ERROR:\tInput not recognized, try agian.")


# This is the main function section
game_start()
i = 1
while i == 1:
    choice = input("Nar:\tPlay again? YES, NO\n").upper()
    if choice == "NO":
        i = 0
    else:
        print()
        print("NEW GAME")
        print()
        game_start()

