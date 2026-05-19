import random
import operator as op_module

OPERATORS = {
    "+": op_module.add,
    "-": op_module.sub,
    "*": op_module.mul,
    "/": op_module.truediv,
}

replay = "yes"

while replay == "yes":  
    print("....................................................................")
    print("welcome to the easy mathematics game")
    print("....................................................................")

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
        symbol = random.choice(list(OPERATORS.keys()))

        print(str(number1) + " " + symbol + " " + str(number2))
        answer = OPERATORS[symbol](number1, number2)
        try:
            user = float(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number.")
            print("Wrong! The correct answer is: ", answer)
            continue
        if user == answer:
            print("Correct!") 
            score += 1  
        else:
            print("Wrong! The correct answer is: ", answer)
      
    
    print("Your score is: ",score )   

    replay = input("do you want to play again? (yes/no): ")