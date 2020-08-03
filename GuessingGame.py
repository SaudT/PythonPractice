import random



def Guess():
    user_input=input("\nGuess the sequence\nyou can choose between Red, Black, Orange, Yellow, Green, Blue, White\nNo repeats, No commas\n")
    #splits so that each word is a element in a list
    user_list = user_input.split()

    #resets counter
    spotOn = 0
    wrongPlace = 0
    x=0

    while x<4:  #Checks for each uesr_input
        y=0     #resets counter to go through all pieces
        while y < 4:  # Checks user_input against computer_choice
            if user_list[x].lower() == comp_choice[y].lower():    #Checks if words match each other
                if x==y:     #if it is at the same index then it is spotOn otherwise its the right color in the wrong place
                    spotOn +=1
                    break
                else:
                    wrongPlace+=1
                    break
            y+=1
        x+=1
                

    print("You got ",spotOn, " in the right place and ",wrongPlace, " in the wrong spot but the right color")
    print(user_list)
    return spotOn


#Computer Code to break
choices = ["Red", "Black", "Orange", "Yellow", "Green", "Blue", "White"]
a = 0
comp_choice = []
skip = False
while a < 4:
    b = 0
    rand_choice = random.randint(0, 6)
    while b < a:
        if comp_choice[b] == choices[rand_choice]:
            skip = True
        b += 1
    if not skip:
        comp_choice.append(choices[rand_choice])
        a += 1
    skip = False



#loop used to guess 10 times

tries = 0 

while tries<10:
    tries+=1
    print("\ntry #:", tries)
    correct = Guess()
    if correct == 4:
        print("Congrats you won in ", tries, "attempts\n")
        break
    if tries == 10:
        print("You Lost")
        break
    
    

print(comp_choice)


