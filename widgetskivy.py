from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image, AsyncImage


def botao_pressionado(instance):
    print("botão pressionado!")

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn=Button(text='clique aqui', font_size=100, size_hint=(0.6, 0.62), background_color=get_color_from_hex("#3498db"), pos_hint={'center_x': 0.5, 'center_y':1.0})
        btn.bind(on_press=botao_pressionado)
        layout.add_widget(btn)
        layout.add_widget(CheckBox(active=False))
        layout.add_widget(Image(source="Captura de tela 2024-03-26 090154.png"))
        layout.add_widget(AsyncImage(source="images.jpeg"))
        
        return layout


if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        btn1 = Button(text='Botão 1', background_color=(0.2, 0.7, 0.3, 1), font_size=20)
        layout.add_widget(btn1)

        btn2 = Button(text='Clique Aqui!', halign='center')
        layout.add_widget(btn2)

        btn3 = Button(text='Clique para Continuar', background_color=(0.9, 0.5, 0.1, 1), font_size=30)
        layout.add_widget(btn3)

        def acao_botao(instance):
            instance.text = 'Botão Pressionado!'

        btn4 = Button(text='Botão 4')
        btn4.bind(on_press=acao_botao)
        layout.add_widget(btn4)

        info_label = Label(text='Pressione os botões para ver diferentes propriedades em ação.')
        layout.add_widget(info_label)

        return layout

if __name__ == '__main__':
    MinhaApp().run()


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MinhaApp(App):
    def build(self):
        layout = GridLayout(cols=2, spacing=[10, 10], padding=[28, 20])
        for i in range(4):
            botao = Button(text=f'Botão {i+1}')
            layout.add_widget(botao)
        return layout

if __name__ == '__main__':
    MinhaApp().run()

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):

        layout_principal = GridLayout(cols=2)


        coluna_esquerda = BoxLayout(orientation="vertical", size_hint=(0.3, 1))

        menu_itens = ['Arquivo', 'Editar', 'Seleção', 'Ver', 'Acessar', 'Sair']

        label_menu = Label(text="Menu")
        coluna_esquerda.add_widget(label_menu)

        for item in menu_itens:
            botao = Button(text=item)
            coluna_esquerda.add_widget(botao)


        coluna_direita = GridLayout(cols=1, rows=3)

        for i in range(3):
            botao = Button(text=f'Botão {i+1}')
            coluna_direita.add_widget(botao)


        layout_principal.add_widget(coluna_esquerda)
        layout_principal.add_widget(coluna_direita)

        return layout_principal

if __name__ == '__main__':
    MinhaApp().run()
