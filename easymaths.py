import random
replay = "yes"

while replay == "yes":  
    print("....................................................................")
    print("welcome to the easy mathematics game")
    print("....................................................................")

    op = ("+", "-", "*", "/")
    difficulty = input("choose your difficulty level (easy, medium, hard):")

    if difficulty == "easy":
        min_val, max_val = 1, 50
    elif difficulty == "medium":
        min_val, max_val = 50, 105
    else:
        min_val, max_val = 100, 200
    score = 0
    for i in range(5):
        
        number1 = random.randint(min_val, max_val)
        number2 = random.randint(min_val, max_val)
        operator = random.choice(op)

        eq = str(number1) + " " + operator + " " + str(number2)
        print(eq)
        answer = eval(eq)
        user = float(input("Your answer: "))
        if user == answer:
            print("Correct!") 
            score += 1  
        else:
            print("Wrong! The correct answer is: ", answer)
      
    
    print("Your score is: ",score )   

    replay = input("do you want to play again? (yes/no): ")