import random

def generate_simple_question():
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    return question, eval(question)

def generate_square_question():
    num = random.randint(11, 29)
    question = f"{num}"
    return question, num ** 2

def main():
    correct_answers = 0

    while True:
        level = input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> ")
        if level in ['1', '2']:
            level = int(level)
            break
        else:
            print("Incorrect format.")

    for _ in range(5):
        if level == 1:
            question, answer = generate_simple_question()
        else:
            question, answer = generate_square_question()

        print(question)
        while True:
            user_answer = input("> ")
            try:
                if int(user_answer) == answer:
                    print("Right!")
                    correct_answers += 1
                else:
                    print("Wrong!")
                break
            except ValueError:
                print("Incorrect format.")

    print(f"Your mark is {correct_answers}/5.")

    save_result = input("Would you like to save your result to the file? Enter yes or no.\n> ").strip().lower()
    if save_result in ['yes', 'y']:
        user_name = input("What is your name?\n> ").strip()
        with open("results.txt", "a") as file:
            level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
            file.write(f"{user_name}: {correct_answers}/5 in level {level} ({level_description}).\n")
        print('The results are saved in "results.txt".')
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
