#Hello
#Today we are going to do Program 3
#Hawaiian Pronounciations

# VARIABLES
Valid = ('AEIOUPKHLMWN \'')

Hawaii = input("Do you have a Hawaiian word? [Y/N] ") #input to ge the loops looping
Hawaii = Hawaii.upper()
print('')
while Hawaii not in ('Y', "YES", 'N', 'NO'): #wow someone was being sassy
    print("Please answer Yes or No")
    print('')
    Hawaii = input("Do you have a Hawaiian word? [Y/N] ")
    Hawaii = Hawaii.upper()
    print('')
while Hawaii in ('Y', 'YES'): #the real work begins, They want to pronounce stuff
    Pronounce = '' #empty string
    z = 0 #start counting at the first letter
    Word = input("What is your Hawaiian word? ")  #find hawaiian word
    Word = Word.upper()
    print('')
    for character in Word: #look through each character
        if not character in Valid: #if its not a goodun
            print("I'm sorry, that is not a valid Hawaiian word.")
            print('')
            Word = input("What is your Hawaiian word? ") #try again
            Word = Word.upper()
            print('')
        break
    while z < len(Word): #while the word is still existing
        #all of the following are the conditions for the pronounciations
        if Word[z] == "A":
            if not (z == len(Word) - 1) and (Word[z+1] == "E" or Word[z+1] == "I"):
                Pronounce += "EYE-"
                z += 2
            elif not (z == len(Word) -1 ) and (Word[z+1] == "O" or Word[z+1] == "U"):
                Pronounce += "OW-"
                z += 2
            else:
                Pronounce += "AH-"
                z += 1
            continue
        if Word[z] == "E":
            if not (z == len(Word) - 1) and Word[z+1] == "I":
                Pronounce += "AY-"
                z += 2
            elif not (z == len(Word) - 1) and Word[z+1] == "U":
                Pronounce += "EH-OO-"
                z += 2
            else:
                Pronounce += "EH-"
                z += 1
            continue
        if Word[z] == "I":
            if not (z == len(Word) - 1) and Word[z+1] == "U":
                Pronounce += "EW-"
                z += 2
            else:
                Pronounce += "EE-"
                z += 1
            continue
        if Word[z] == "O":
            if not (z == len(Word) - 1) and Word[z+1] == "I":
                Pronounce += "OY-"
                z += 2
            elif not (z == len(Word) - 1) and Word[z+1] == "U":
                Pronounce += "OW-"
                z += 2
            else:
                Pronounce += "OH-"
                z += 1
            continue
        if Word[z] == "U":
            if not (z == len(Word) - 1) and Word[z+1] == "I":
                Pronounce += "OOEY-"
                z += 2
            else:
                Pronounce += "OO-"
                z += 1
            continue
        if Word[z] == "P":
            Pronounce += "P"
            z += 1
            continue
        if Word[z] == "K":
            Pronounce += "K"
            z += 1
            continue
        if Word[z] == "H":
            Pronounce += "H"
            z += 1
            continue
        if Word[z] == "L":
            Pronounce += "L"
            z += 1
            continue
        if Word[z] == "M":
            Pronounce += "M"
            z += 1
            continue
        if Word[z] == "N":
            Pronounce += "N"
            z += 1
            continue
        if Word[z] == "W":
            if (Word[z-1] == "I" or Word[z-1] == "E"):
                Pronounce += "V"
                z += 1
            else:
                Pronounce += "W"
                z += 1
            continue
        if Word[z] == ' ':
            Pronounce += ' '
            z += 1
            continue
        if Word [z] == "\'":
            Pronounce += "\' "
            z += 1
            continue
    Pronounce = Pronounce[:-1] #get rid of that pesky last -
    print("{} is pronounced {}".format(Word,Pronounce.capitalize())) #this is your word, this is your pronounciation
    print('')
    Hawaii = input("Do you have another Hawaiian word? [Y/N] ") #would you like to play again?
    Hawaii = Hawaii.upper()
    print('')
    while Hawaii not in ('Y', "YES", 'N', 'NO'):
        print("Please answer Yes or No")
        print('')
        Hawaii = input("Do you have a Hawaiian word? [Y/N] ")
        Hawaii = Hawaii.upper()
        print('')
