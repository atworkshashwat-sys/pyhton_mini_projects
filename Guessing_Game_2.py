import random
replay = "yes"
while replay == "yes":  
    print("....................................................................")
    print("welcome to the second edition of the guessing game")
    print("....................................................................")
    print("this time we have better experience packed for you ")
    print("....................................................................")
    print("you have 5 attempts to guess the number")
    print("....................................................................")
    print("[in easy mode number will be guessed between 1 to 50]")
    print("....................................................................")
    print("[in medium mode number will be guessed between 1 to 105]")
    print("....................................................................")
    print("[in hard mode number will be guessed between 1 to 200]")
    print("....................................................................")
    difficulty = input("choose your difficulty level (easy, medium, hard):")
    if difficulty == "easy":
        number = random.randint(1,50)
    elif difficulty == "medium":
        number = random.randint(1,105)
    else:
        number = random.randint(1,200)
    attempts = 0  
    while attempts<5:
        #try helps you to avoid crashing the program when user enters a non-integer value
        try:
            usernumber = int(input("guess the number:"))
            #it helps in keeping the program running 
        except ValueError:
            print("please enter a valid number")
            continue

        if usernumber<number:
            print("little low")
            attempts = attempts + 1
        elif usernumber>number:
            print("little high")
            attempts = attempts + 1
        else:
            print("correct!")
            break
    
    if usernumber != number:
        print("you lost")
        print("the number was", number)
        attempts = 0
    
    replay = input("do you want to play again? (yes/no): ")