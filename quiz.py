import questions

def ask_question(question):
    print(question["question"])
    for idx, choice in enumerate(question["choices"], 1):
        print(f"{idx}. {choice}")
    
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if answer in range(1, 5):
                return question["choices"][answer - 1] == question["answer"]
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    score = 0
    for question in questions.questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    
    print(f"Your final score is {score} out of {len(questions.questions)}")

if __name__ == "__main__":
    main()