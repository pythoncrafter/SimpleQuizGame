from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

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

class QuizApp(App):
    def build(self):
        self.questions = [
            Question("What is the capital of France?", ["Paris", "Berlin", "Rome"], 1),
            Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter"], 1),
            Question("Which is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe"], 2)
        ]
        self.score = 0

        layout = BoxLayout(orientation='vertical')
        self.question_label = Label(text="Simple Quiz Game", font_size=30)
        layout.add_widget(self.question_label)

        for idx, question in enumerate(self.questions, start=1):
            question_label = Label(text=f"Question {idx}: {question.question}")
            layout.add_widget(question_label)
            for i, option in enumerate(question.options, start=1):
                btn = Button(text=option)
                btn.bind(on_press=self.check_answer_wrapper(idx, i))
                layout.add_widget(btn)

        return layout

    def check_answer_wrapper(self, question_idx, user_choice):
        def inner(instance):
            question = self.questions[question_idx - 1]
            if question.check_answer(user_choice):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect.")

        return inner

if __name__ == '__main__':
    QuizApp().run()
