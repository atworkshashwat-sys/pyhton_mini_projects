import random
import operator

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

VALID_DIFFICULTIES = ("easy", "medium", "hard")


def get_difficulty():
    """Prompt the user for a valid difficulty level."""
    while True:
        difficulty = input("Choose your difficulty level (easy, medium, hard): ").strip().lower()
        if difficulty in VALID_DIFFICULTIES:
            return difficulty
        print(f"Invalid choice '{difficulty}'. Please enter easy, medium, or hard.")


def get_numeric_answer():
    """Prompt the user for a numeric answer, retrying on invalid input."""
    while True:
        raw = input("Your answer: ").strip()
        try:
            return float(raw)
        except ValueError:
            print(f"'{raw}' is not a valid number. Please enter a numeric answer.")


def get_yes_no(prompt):
    """Prompt the user for a yes/no response, retrying on invalid input."""
    while True:
        response = input(prompt).strip().lower()
        if response in ("yes", "no"):
            return response
        print(f"Invalid response '{response}'. Please enter yes or no.")


def generate_question(min_val, max_val):
    """Generate a math question and its rounded answer."""
    number1 = random.randint(min_val, max_val)
    number2 = random.randint(min_val, max_val)
    symbol = random.choice(list(OPERATORS.keys()))

    # Avoid division by zero by regenerating number2 if it is zero
    while symbol == "/" and number2 == 0:
        number2 = random.randint(min_val, max_val)

    equation = f"{number1} {symbol} {number2}"
    answer = OPERATORS[symbol](number1, number2)
    # Round to 2 decimal places so comparisons are fair for division
    answer = round(answer, 2)
    return equation, answer


def play_round():
    """Play a single round of 5 questions."""
    difficulty = get_difficulty()

    if difficulty == "easy":
        min_val, max_val = 1, 50
    elif difficulty == "medium":
        min_val, max_val = 50, 105
    else:
        min_val, max_val = 100, 200

    score = 0
    for _ in range(5):
        equation, answer = generate_question(min_val, max_val)
        print(equation)

        if "/" in equation:
            print("(Round your answer to 2 decimal places)")

        user_answer = get_numeric_answer()
        user_answer = round(user_answer, 2)

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

    print(f"Your score is: {score}/5")


def main():
    """Main game loop."""
    while True:
        print("....................................................................")
        print("Welcome to the Easy Mathematics Game")
        print("....................................................................")

        play_round()

        replay = get_yes_no("Do you want to play again? (yes/no): ")
        if replay == "no":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
