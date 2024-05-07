from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class RotuloApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.lab1 = Label(
            text='SENAI', color=[1, 0, 0, 1],
            font_size=40, bold=True
        )

        self.lab2 = Label(
            text='SESI', color=[0, 1, 0, 1],
            font_size=40, italic=True
        )

        self.lab3 = Label(
            text='ENEM', color=[0, 0, 1, 1],
            font_size=40, font_name="arial",
            underline=True
        )

        layout.add_widget(self.lab1)
        layout.add_widget(self.lab2)
        layout.add_widget(self.lab3)
        return layout

if __name__ == "__main__":
    RotuloApp().run()

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        layout_float = FloatLayout()
        
        botaol = Button(text="Botão 1", size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.1, 'y': 0.8})
        botao2 = Button(text="Botão 2", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        botao3 = Button(text='Botão 3', size_hint=(None, None), size=(100, 50), pos_hint={'right': 0.9, 'y': 0.1})

        layout_float.add_widget(botaol)
        layout_float.add_widget(botao2)
        layout_float.add_widget(botao3)

        return layout_float

if __name__ == "__main__":
    MinhaApp().run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (720, 400)

class calcy(GridLayout):
    def __init__(self, **kwargs):
        super(calcy, self).__init__(**kwargs)
        self.first = self.second = 0

    def onpress(self, instance):
        if instance.text == 'C':
            self.ids.t1.text = ''
            self.first = self.second = 0
        elif instance.text in "+-*/":
            self.first = int(self.ids.t1.text)
            self.ids.t1.text = '0'
            self.op = instance.text
        elif instance.text == '=':
            if self.first == 0:
                return
            self.second = int(self.ids.t1.text)
            if self.op == '+':
                result = self.first + self.second
            if self.op == '-':
                result = self.first - self.second
            if self.op == '*':
                result = self.first * self.second
            if self.op == '/':
                if self.second == 0:
                    return
                result = self.first / self.second
            self.ids.t1.text = str(result)
            self.first = self.second = 0
        else:
            self.ids.t1.text = self.ids.t1.text + instance.text

class calculatorapp(App):
    def build(self):
        return calcy(cols=3)

calculatorapp().run()