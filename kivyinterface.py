from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window

class RegistroUsuario(App):
    def build(self):
        Window.clearcolor= (1, 1, 1, 1)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        titulo = Label(text='Formulário de Registro', halign='center', color=(0, 0, 0.2, 1), bold=True, font_size=26)
        layout.add_widget(titulo)

        self.nome_input = TextInput(hint_text='Digite seu nome...')
        layout.add_widget(Label(text='Nome:', color=(0, 0, 0.2, 1), bold=True, font_size=26))
        layout.add_widget(self.nome_input)

        self.email_input = TextInput(hint_text='Digite seu e-mail...', input_type='text')
        layout.add_widget(Label(text='E-mail:', color=(0, 0, 0.2, 1), bold=True, font_size=26))
        layout.add_widget(self.email_input)

        self.senha_input = TextInput(hint_text='Digite sua senha...', password=True)
        layout.add_widget(Label(text='Senha:', color=(0, 0, 0.2, 1), bold=True, font_size=26))
        layout.add_widget(self.senha_input)

        self.confirma_senha_input = TextInput(hint_text='Confirme sua senha...', password=True)
        layout.add_widget(Label(text='Confirmar Senha:', color=(0, 0, 0.2, 1), bold=True, font_size=26 ))
        layout.add_widget(self.confirma_senha_input)

        botao_registro = Button(text='Registrar', size_hint=(None, None), size=(150, 50))
        botao_registro.bind(on_press=self.cadastrar_usuario)
        layout.add_widget(botao_registro)

        return layout

    def cadastrar_usuario(self, instance):
        nome = self.nome_input.text.strip()
        email = self.email_input.text.strip()
        senha = self.senha_input.text.strip()
        confirma_senha = self.confirma_senha_input.text.strip()

        if nome and email and senha and confirma_senha:
            if senha == confirma_senha:
                self.mostrar_popup("Sucesso", "Usuário registrado com sucesso!")
            else:
                self.mostrar_popup("Erro", "Senha e confirmar senha não coincidem!")
        else:
            self.mostrar_popup("Erro", "Preencha todos os campos!")

    def mostrar_popup(self, titulo, mensagem):
        popup = Popup(title=titulo, content=Label(text=mensagem), size_hint=(None, None), size=(400, 200))
        popup.open()


if __name__ == "__main__":
    RegistroUsuario().run()



