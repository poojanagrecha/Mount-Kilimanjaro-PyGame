#Store answers in variables
yes = ["Yes", "YES", "yes", "yeah", "Y", "y", "Yeah"]
no = ["No", "NO", "no", "N", "n"]
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
options = ("\n Please use A, B, or C")

#Introduction
print("What is your name?")
name = input(">>> ")

#Option to replay game
def playAgain():
    choice = input("You have lost. Would you like to play again? Yes/No ")
    if choice in yes:
        intro()
    elif choice in no:
        print("Come back to play later!")
    else: 
        print("I did not understand that")
        playAgain()
    
#Start of game       
def intro():
    print("\n" + name.capitalize()+ ", you are embarking on a journey to climb the snowy Mount Kilimanjaro! You have 3 people on your team and are competing against other teams to who reaches the top first. The reward is a whopping 1 million dollars!! On your way to the top you realize you are running out of water. What do you do?" )
    print("\nA. Pack the snow in your water bottle and allow it to melt.\nB. Control your water portions till the next watering station is available.\nC. Drink the rest of your water to fuel you for the time being.")
    choice = input(">>> ")
    if choice in answer_A:
        answer= input("Eeeyuck! Snow water is contaminated and you have died! Would you like to change your answer? Yes/No ")
        if answer in yes:
            intro()
        else:
            playAgain()
    elif choice in answer_B:
        keepGoing() 
    elif choice in answer_C:
        answer= input("Watering station too far and you have run out of fuel! Would you like to change your answer? Yes/No ")
        if answer in yes:
            intro()
        else:
            playAgain()
    else:
        print(options)
        intro()

#First option
def keepGoing():
    print("\nGreat choice " + name.capitalize() + "! Your team member has decided to quit the climb, however if you are not in a team of three you will not win. What do you do?")
    print("\nA. Carry them up. \nB. Bribe them to continue. \nC. Allow your team to end the trek early for the day and continue tomorrow")
    choice = input(">>> ")
    if choice in answer_A:
        answer= input("Team member too heavy! Would you like to change your answer? Yes/No ")
        if answer in yes:
            keepGoing()
        else:
            playAgain()
    elif choice in answer_B:
        snowstorm()
    elif choice in answer_C:
        snowMobile()
    else:
        print(options)
        keepGoing()

#Snowmobile challenge
def snowMobile():
    print("\nYou're behind now! However, you notice a snowmobile driver offering your team a ride to the next camp stop. Since you are the last ones, you know no one will see you driving up there! Do you take the opportunity?")
    print("A. Yes! Its worth the prize!! \nB. Slow and steady wins the race... no cheating! \nC. Ask the snowmobile driver to only drop you halfway to make you feel less guilty")
    choice = input(">>> ")
    if choice in answer_A:
        finalFlag()
    elif choice in answer_B:
        answer= input("Slow and steady doesn't win in this case! Would you like to change your answer? Yes/No ")
        if answer in yes:
            snowMobile()
        else:
            playAgain()
    elif choice in answer_C:
        answer= input("Snowmobile driver doesn't want to make any stops! He has places to go too! Would you like to change your answer? Yes/No ")
        if answer in yes:
            snowMobile()
        else:
            playAgain()
    else:
        print(options)
        snowMobile()

#Snowstorm challenge
def snowstorm():
    print("\nWhile continuing your trek, you get an alert that there is a huge snow storm coming your way! Luckily you are closer to the bottom than most others...however you feel bad for the other teams and are curious to see if they need help. What do you do?")
    print("\nA. Wait for the other teams to reach you, then find ways to hurry down! \nB. Head down, you need to be safe! \nC. Try to find a snowcabin that will keep you safe from the storm, then alert the other teams to meet you there.")
    choice = input(">>> ")
    if choice in answer_A:
        answer= input("You will die if you wait for other teams! Would you like to change your answer? Yes/No ")
        if answer in yes:
            snowstorm()
        else:
            playAgain()
    elif choice in answer_B:
        print("Great choice! " + name.capitalize() + ", you are now safe at the start of the trek. Even though you're at the bottom, all the other teams died in the snowstorm. \nTherefore you have won the challenge.")
    elif choice in answer_C:
        finalFlag()
    else:
        print(options)
        snowstorm()

#Final Flag challenge
def finalFlag():
    print("You are almost at the top! However a new challenge has come your way... 1 mile left and there are three flags. Each team can only choose one flag, however to be the winner you must choose the right colored flag that matches the one at the top. Which color do you choose?")
    print("\nA. Green \nB. Purple \nC. Red")
    choice = input(">>> ")
    if choice in answer_A:
        print("This is the correct flag! \nYou and your team have won the challenge. Congrats " + name.capitalize() + "!")
    elif choice in answer_B:
        answer= input("Wrong flag! Would you like to change your answer? Yes/No ")
        if answer in yes:
            finalFlag()
        else:
            playAgain()
    elif choice in answer_C:
        answer= input("Wrong flag! Would you like to change your answer? Yes/No ")
        if answer in yes:
            finalFlag()
        else:
            playAgain()
    else:
        print(options)
        finalFlag()
intro()

