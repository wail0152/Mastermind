antwoord = []
for i in range(0, 4):
    antwoordIn = input("Geef vier kleuren (getallen 1-6).")
    antwoordIn = int(antwoordIn)
    antwoord.append(antwoordIn)
print(antwoord)


def mogelijkheden(): #finished
    mList = []
    list = [0, 0, 0, 0]
    for i in range(0, 6):
        list[0] += 1
        for i2 in range(0,6):
            list[1] += 1
            if list[1] == 7:
                list[1] = 1
            for i3 in range(0,6):
                list[2] += 1
                if list[2] == 7:
                    list[2] = 1
                for i4 in range(0, 6):
                    list[3] += 1
                    if list[3] == 7:
                        list[3] = 1
                    mList.append(list[:])
    return mList


def guess(mogelijkheden): #In progress
    guesses = 0
    if guesses == 0:
        return mogelijkheden[0]


def feedback(): #Needs to be worked on / In progress
    fb = "None"
    if guess(mogelijkheden()) == antwoord:
        print("Geraden")
    else:
        for i in guess(mogelijkheden()):
            indxi = guess(mogelijkheden()).index(i)
            for j in antwoord:
                indxj = antwoord.index(j)
                if indxi == indxj:
                    print("Witte pin")
                    fb = "White"
                elif i == j and indxi != indxj:
                    print("Zwarte pin")
                    fb = "Black"
                else:
                    print("Geen pin")
    return fb




print(mogelijkheden())
print(guess(mogelijkheden()))
print(feedback())
