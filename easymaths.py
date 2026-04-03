import random
replay = "yes"
while replay == "yes":  
    print("....................................................................")
    print("welcome to the easy mathematics game")
    print("....................................................................")
    print("this game is for the students of age around 8 to 12 so fo them to imporve there mathematical skills")
    print("....................................................................")
    print("you have 5 attempts to guess the number")
    print("....................................................................")
    print("[in easy mode numbers will be taken between 1 to 50]")
    print("....................................................................")
    print("[in medium mode numbers will be taken between 50 to 105]")
    print("....................................................................")
    print("[in hard mode numbers will be taken between 100 to 200]")
    print("....................................................................")
    op = ("+", "-", "*", "/")
    difficulty = input("choose your difficulty level (easy, medium, hard):")
    if difficulty == "easy":
        number1 = random.randint(1,50)
        number2 = random.randint(1,50)
        operation = random.choice(op)
        eq = str(number1) + " " + operation + " " + str(number2)
        print("what is", eq)
        
    elif difficulty == "medium":
        number1 = random.randint(50,105)
        number2 = random.randint(50,105)
        operation = random.choice(op)
        eq = str(number1) + " " + operation + " " + str(number2)
        print("what is", eq)

    else:
        number1 = random.randint(100,200)
        number2 = random.randint(100,200) 
        operation = random.choice(op)  
        eq = str(number1) + " " + operation + " " + str(number2)
        print("what is", eq)
#this function helpss in solving the generated equations
    answer = eval(eq)
    attempts = 0  
    
    while attempts<5:
        try:
            useranswer = float(input("enter your answer:"))
        except:
            print("please enter a valid number") 
        if useranswer == answer:
            print("correct!")
            break
        else:
            print("try again do not fear it!")
        attempts = attempts + 1
    
    replay = input("do you want to play again? (yes/no): ")