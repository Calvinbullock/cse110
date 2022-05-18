# CAlvin Bullock
# April 2022
# 02 Prove Assignment 

print("Please enter the following:")

adjective = input("Adjective: ")
animal = input("Animal: ")
verb_1 = input("Verb: ")
exclamation = input("Exclamation: ").capitalize()
verb_2 = input("Verb: ")
verb_3 = input("Verb: ")
animal_2 = input("Animal: ").lower()

# sets the indefinite article in the last sentance between "an" or "a" based on if the seconed animal starts with a vowel 
indefinite_article = "a"
if animal_2[0] == "a" or animal_2[0] == "e" or animal_2[0] == "i" or animal_2[0] == "o" or animal_2[0] == "u":
    indefinite_article = "an"

print("The other day, I was really in trouble. It all started when I saw a very")
print("{0} {1} {2} down the hallway. \"{3}!\" I yelled. But all".format(adjective, animal, verb_1, exclamation))
print("I could think to do was to {0} over and over. Miraculously,".format(verb_2))
print("that caused it to stop, but not before it tried to {0}".format(verb_3))
print("right in front of my family.")
print("But the {0} then {1} stright at me and {2} into me.".format(animal, verb_3, verb_2))
print("Right when I finally thought this was over {0} {1} come over and gave me".format(indefinite_article, animal_2))
print("a nice big hug.")