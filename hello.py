from kivy.app import App
from kivy.uix.button import Button
class MyApp(App):
    def build(self):
        return Button(text="Hello World! this is my frist program in kivy \n and i love my theacher")

if __name__ == "__main__":
    MyApp().run()
