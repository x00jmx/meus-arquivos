from kivy.app import App
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        return TextInput(text="tudo bom?")

if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '300')
Config.set('graphics', 'resizable', '1')

class MyDemoApp(App):
    def build(self):
        main = BoxLayout(orientation='vertical')
        self.text1 = TextInput(multiline=True, font_size=20)
        btns = BoxLayout(orientation='horizontal')

        self.b1 = Button(text='COPY')
        self.b1.bind(on_press=lambda instance: self.gettext(instance))
        self.b2 = Button(text='PASTE')
        self.b2.bind(on_press=lambda instance: self.insert(instance))
        self.text2 = TextInput(
            multiline=True, font_size=20,
            foreground_color=[0, 0, 1, 1]
        )

        btns.add_widget(self.b1)
        btns.add_widget(self.b2)
        main.add_widget(self.text1)
        main.add_widget(btns)
        main.add_widget(self.text2)
        return main

    def gettext(self, instance):
        self.text_to_paste = self.text1.selection_text

    def insert(self, instance):
        self.text2.insert_text(self.text_to_paste)

if __name__ == '__main__':
    MyDemoApp().run()


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MinhaApp(App):
    def build(self):
        
        layout_principal = BoxLayout(orientation='vertical')
        
        self.input_nome = TextInput(hint_text='Digite seu nome')
        layout_principal.add_widget(self.input_nome)
        
        botao_enviar = Button(text='Enviar', on_press=self.exibir_mensagem)
        layout_principal.add_widget(botao_enviar)
        
        self.label_mensagem = Label()
        layout_principal.add_widget(self.label_mensagem)
        return layout_principal

    def exibir_mensagem(self, instance):
        nome_usuario = self.input_nome.text
        mensagem = f'Olá {nome_usuario}, você está avançando no Kivy! Parabéns SESIAΝΟ!!!'
        self.label_mensagem.text = mensagem

if __name__ == '__main__':
    MinhaApp().run()

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class MyApp(App):
    def build(self):
        return ToggleButton(text='ligado', state="normal")

if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.uix.switch import Switch

class MyApp(App):
    def build(self):
        return Switch(active=False)

if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (700, 300)

class ModalViewDemoApp(App):
    def showmodal(self, obj):
        view = ModalView(
            auto_dismiss=False, size_hint=(None, None),
            size=(400, 100)
        )
        grid = GridLayout(cols=1, padding=10)
        grid.add_widget(Label(
            text='parabens você concluiu seu cadastro', font_size=32,
            color=[1, 0, 0, 1]
        ))
        btn = Button(
            text='ok', font_size=32,
            on_press=view.dismiss
        )
        grid.add_widget(btn)
        view.add_widget(grid)
        view.open()

    def build(self):
        btn = Button(
            text='click here', font_size=32,
            on_press=self.showmodal,
            pos_hint={'center_x': .5, 'center_y': .1},
            size_hint=(.3, None), size=(200, 100)
        )
        return btn

if __name__ == '__main__':
    ModalViewDemoApp().run()
