import random
colors = ["white", "red", "blue", "black", "green", "yellow", "orange"]
i = 0
computers = []
guesses = 0
checker = [False, False, False, False]
second_check = [False, False, False, False]
while i < 4:
    number = random.randint(0, 6)
    computers.append(colors[number])
    i += 1
print(computers)
while guesses < 7:
    i = 0
    x = 0
    j = 0
    cplace = 0
    ccolor = 0
    user = input("pick four colors white, red, blue, black, green, yellow, orange\n")
    glist = user.split() # glist is guess list 
    if len(glist) != 4:
        print("message too long or too short,  pick exactly 4")
    else:
        while i < 4:  # checks if places match
            if computers[i] == glist[i]:
                cplace = cplace + 1
                ccolor += 1
                checker[i] = True
            i += 1
        print("checker",checker)
        while x < 4:  # runs through all iterations of the computer array
            j = 0
            while j < 4:  # runs and checks through iteratons of guess array
                if computers[j] == glist[x] and (checker[j] is False):
                    # second_check[j] = True
                    print("glist",glist)
                    print("checker",checker)
                    checker[j] = True
                    ccolor += 1
                j += 1
            x += 1
            #second_check = [False, False, False, False]
        checker = [False, False, False, False]
        print("ccolor", ccolor)
        print("Cplace:", cplace)
        if cplace == 4:
            print("YOU WINNNN")
            break
        else:
            print("you have " + str(cplace) + " in the correct place")
            print("you have " + str(ccolor) + " correct colors")

    guesses += 1

if guesses == 7:
    print("out of guesses, Sorry")
