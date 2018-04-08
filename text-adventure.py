#Import Section
import random
import time

#Functions Section

#Intro Message
def introMessage():
    print("Long...long...long time ago...The Arcadia Empire was facing some very dark times")
    print("You, a mystic soldier, emerged from deep in the woods to find yourself on a crossroad.")
    print("(1) One path leads back to your kingdom, were you'll be rewarded handsomly for your bravery in battle.")
    print("And (2) the other one, leads to a dark portal that emanates a purpleish light")
    print()

#Choose Path input validation
def choosePath():
    path = ""
    # input validation
    while path != "1" and path != "2": 
        path = input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath):
    print("You head down the dirt road,")
    time.sleep(3)
    print("there's a tall and ancient tree nearby that looks familiar, that must be a good sign...")
    time.sleep(3)
    print("But your skin begins to tingle and vision starts to get blurry...")
    print()
    time.sleep(3)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("That tingling was the fae particles of the glamour layer used to camouflage your kingdom")
        print("Welcome home hero!")
        print("There is a big celebration on your name, and you live the rest of your life in peace.")
        print()
    else:
        print("You step inside the dark portal, and you feel the dark energy starting to seep through your skin")
        print("causing all of the atoms in your body to dissociate")
        print("there is no record left of your existence.")
        print("You fell into the evil mage's trap, and now your kingdom will be at the mercy of his powers.")
        print()

#Code area that uses above functions
playAgain = "yes"

#Checks to see if user want to play again and runs the initial functions to restart the game.
while playAgain == "yes" or playAgain == "y":
    introMessage()
    choice = choosePath()

    # choice is equal to "1" or "2"
    checkPath(choice) 
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")



