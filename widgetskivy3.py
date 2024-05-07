from kivy.app import App
from kivy.uix.progressbar import ProgressBar

class MyApp(App):
    def build(self):
        return ProgressBar(value=90)

if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)

        slider = Slider(min=0, max=100, value=5, step=1)
        slider.bind(value=self.atualizar_label)

        self.label = Label(text="valor do slide: {}".format(int(slider.value)))

        layout.add_widget(slider)
        layout.add_widget(self.label)

        return layout

    def atualizar_label(self, instance, valor):
        self.label.text = "valor do slide: {}".format(int(valor))

if __name__ == '__main__':
    MyApp().run()

