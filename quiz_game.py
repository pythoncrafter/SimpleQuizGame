from kivy.config import Config
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
import sqlite3
from sqlite3 import Error
import os

class Question:
    def __init__(self, question, options, correct_option, category):
        self.question = question
        self.options = options.split(',')
        self.correct_option = correct_option
        self.category = category

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
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'questions.db')
        conn = None
        try:
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM questions")
            rows = cursor.fetchall()
            self.questions = [Question(row[1], row[2], row[3], row[4]) for row in rows]
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def add_question(self, question, options, correct_option, category):
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'questions.db')
        conn = None
        try:
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO questions (question, options, correct_option, category) VALUES (?,?,?,?)", (question, options, correct_option, category))
            conn.commit()
            print("Question added successfully")
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

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
    if platform == 'macosx':
        # Set the window size for macOS
        Window.size = (800, 600)
    elif platform == 'ios' or platform == 'android':
        # Set the window size for mobile platforms
        Window.fullscreen = 'auto'

    QuizApp().run()
