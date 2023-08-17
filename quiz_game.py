class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.question)
        for idx, option in enumerate(self.options, start=1):
            print(f"{idx}. {option}")
        
    def check_answer(self, user_choice):
        return user_choice == self.correct_option

if __name__ == "__main__":
    questions = [
        Question("What is the capital of France?", ["Paris", "Berlin", "Rome"], 1),
        Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter"], 1),
        Question("Which is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe"], 2)
    ]
    
    print("Simple Quiz Game")
    score = 0

    for idx, question in enumerate(questions, start=1):
        print(f"\nQuestion {idx}:")
        question.display_question()
        user_choice = int(input("Enter your choice: "))
        if question.check_answer(user_choice):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

    print(f"\nYour final score: {score}/{len(questions)}")
