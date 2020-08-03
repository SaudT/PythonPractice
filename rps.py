#Rock Paper Scissors game
import random
import string

def game():
    your_choice = input("Rock, Paper, or Scissors: ")
    choices = ["rock", "paper", "scissor"]

    rps = 0
    rps = random.randint(0,2)
    print()

    comp_choice = choices[rps]

    print("You chose: "+ your_choice)
    print("Computer chose: "+ comp_choice)

    if comp_choice == your_choice.lower():
        print("Tie")
    else:
        if comp_choice == "rock":
            if your_choice.lower() == "paper":
                print ("You Win")
            elif your_choice.lower() == "scissor":
                print("You Lost")

        if comp_choice == "paper":
            if your_choice.lower() == "scissor":
                print("You Win")
            elif your_choice.lower() == "rock":
                print("You Lost")

        if comp_choice == "scissor":
            if your_choice.lower() == "rock":
                print("You Win")
            elif your_choice.lower() == "paper":
                print("You Lost")
    print()
    return


x = 1
while x != "0":
    game()
    print("Would you like to continue")
    print("Press 0 to End game, Press 1 to continue")
    x = input()
print("Thank you for playing")
