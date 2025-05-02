from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text='Hello, Kivy!')
        self.add_widget(self.label)

        self.button = Button(text='Click Me')
        self.button.bind(on_press=self.on_button_click)
        self.add_widget(self.button)

    def on_button_click(self, instance):
        self.label.text = 'Button Clicked!'

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()