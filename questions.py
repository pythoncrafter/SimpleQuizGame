from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class QuizApp(App):
    def build(self):
        return MainScreen()

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Welcome to the Quiz App'))
        self.add_widget(Button(text='Login with Google'))
        self.add_widget(Button(text='Login with macOS Account'))

if __name__ == '__main__':
    QuizApp().run()
