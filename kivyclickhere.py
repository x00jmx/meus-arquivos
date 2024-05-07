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
