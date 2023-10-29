from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import json
import os

DEFAULT_QUESTIONS = [
    {
        "question": "What is the diameter of a basketball hoop in inches?",
        "options": ["15", "16", "18"],
        "correct_option": 3
    },
    {
        "question": "How many players are allowed on the court from each team in a basketball game?",
        "options": ["4", "5", "6"],
        "correct_option": 2
    },
    {
        "question": "Which player has won the most NBA championships in history?",
        "options": ["Michael Jordan", "LeBron James", "Bill Russell"],
        "correct_option": 3
    },
    {
        "question": "How many quarters are there in a standard basketball game?",
        "options": ["2", "3", "4"],
        "correct_option": 3
    },
    {
        "question": "Which team has won the most NBA championships as of 2022?",
        "options": ["Los Angeles Lakers", "Boston Celtics", "Chicago Bulls"],
        "correct_option": 2
    }
]

class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def check_answer(self, user_choice):
        return user_choice == self.correct_option

class QuizApp(App):
    def build(self):
        self.load_questions()
        self.score = 0
        self.current_question = 0

        layout = GridLayout(cols=1)

        self.question_label = Label(text="Simple Quiz Game", font_size=30)
        layout.add_widget(self.question_label)

        self.options_layout = GridLayout(cols=1)

        layout.add_widget(self.options_layout)

        self.show_question()
        return layout

    def load_questions(self):
        file_path = 'questions.json'
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump(DEFAULT_QUESTIONS, file)

        with open(file_path, 'r') as file:
            data = json.load(file)
            self.questions = [Question(item['question'], item['options'], item['correct_option']) for item in data]


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
            self.save_results()

    def show_result_popup(self):
        content = Label(text=f"Your final score: {self.score}/{len(self.questions)}", font_size=20)
        popup = Popup(title='Quiz Result', content=content, size_hint=(None, None), size=(400, 400))
        popup.open()

    def save_results(self):
        results = {'score': self.score, 'total_questions': len(self.questions)}
        with open('results.json', 'w') as file:
            json.dump(results, file)

if __name__ == '__main__':
    QuizApp().run()
