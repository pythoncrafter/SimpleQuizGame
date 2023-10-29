from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle

class QuizApp(App):
    def build(self):
        return MainScreen()

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 50, 50, 50]
        self.spacing = 30
        self.add_widget(Label(text='Welcome to the Quiz App', 
                              size_hint=(1, 0.25), 
                              font_size='24sp'))
        self.add_widget(CustomButton(text='Login with Google', 
                                     background_color=(0.2, 0.7, 0.3, 1),
                                     on_release=self.login_with_google))
        self.add_widget(CustomButton(text='Login with macOS Account', 
                                     background_color=(0.2, 0.6, 0.9, 1),
                                     on_release=self.login_with_macos))

    def login_with_google(self, instance):
        print("Login with Google")

    def login_with_macos(self, instance):
        print("Login with macOS Account")

class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = kwargs.get('background_color')
        self.size_hint = (1, 0.2)
        self.border = (10, 10, 10, 10)
        self.border_radius = 20

if __name__ == '__main__':
    QuizApp().run()
