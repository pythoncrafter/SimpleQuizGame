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
        self.padding = [50, 50, 50, 50]
        self.spacing = 30
        self.add_widget(Label(text='Welcome to the Quiz App', 
                              size_hint=(1, 0.4), 
                              font_size='24sp'))
        self.add_widget(Button(text='Login with Google', 
                               size_hint=(1, 0.2),
                               background_color=(0.2, 0.7, 0.3, 1),
                               font_size='18sp',
                               on_release=self.login_with_google))
        self.add_widget(Button(text='Login with macOS Account', 
                               size_hint=(1, 0.2),
                               background_color=(0.2, 0.6, 0.9, 1),
                               font_size='18sp',
                               on_release=self.login_with_macos))

    def login_with_google(self, instance):
        print("Login with Google")

    def login_with_macos(self, instance):
        print("Login with macOS Account")

if __name__ == '__main__':
    QuizApp().run()
