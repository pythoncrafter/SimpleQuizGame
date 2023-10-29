from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

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
        self.current_question = 0

        layout = GridLayout(cols=1)

        self.question_label = Label(text="Simple Quiz Game", font_size=30)
        layout.add_widget(self.question_label)

        self.options_layout = GridLayout(cols=1)

        layout.add_widget(self.options_layout)

        self.show_question()
        return layout

    def show_question(self):
        self.options_layout.clear_widgets()
        question = self.questions[self.current_question]

        question_label = Label(text=f"Question {self.current_question + 1}: {question.question}", font_size=20)
        self.options_layout.add_widget(question_label)

        for i, option in enumerate(question.options, start=1):
            btn = Button(text=option, size_hint_y=None, height=40)
            btn.bind(on_press=lambda instance, i=i: self.check_answer(i))
            self.options_layout.add_widget(btn)

    def check_answer(self, user_choice):
        question = self.questions[self.current_question]
        if question.check_answer(user_choice):
            self.score += 1

        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.show_question()
        else:
            self.show_result_popup()

    def show_result_popup(self):
        content = Label(text=f"Your final score: {self.score}/{len(self.questions)}", font_size=20)
        popup = Popup(title='Quiz Result', content=content, size_hint=(None, None), size=(400, 400))
        popup.open()

if __name__ == '__main__':
    QuizApp().run()
