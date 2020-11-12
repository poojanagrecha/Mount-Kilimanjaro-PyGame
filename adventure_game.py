#Introduction
print("What is your name?")
name = input(">>> ")
print("Welcome " + name + ". Lets begin an adventure shall we?")
answer = input(">>> ")
if answer == "yes":
    print(name+ ", you have decided to embark on a journey of hiking through the Mt Kilimanjaro in the cold months of December.You have 3 people on your team and are competing against other teams to who reaches the top first. On your way to the top you realize you are running out of water. What do you do?")
else:
        print("Darn! Come back when you are ready to play!")

print("A. Pack the snow in your water bottle and allow it to melt.\nB. Control your water portions till the next watering station is available.\nC. Drink the rest of your water to fuel you for the time being.")
choice = input(">>> ")
if choice == "A":
    print("Eeeyuck! Snow is contaminated! You have fallen sick and need to rest. You have lost")
elif choice == "B":
    print("Good choice! Watering station is three more miles away. Keep going!")
elif choice == "C":
    print("Watering station is too far! You have become dehydrated and will need to rest. You have lost")
else:
    print("Sorry I did not understand. Please choose A, B, or C")
