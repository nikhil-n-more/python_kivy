from cgitb import text
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Name: "))

        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favourite: "))

        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Address: "))

        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

class SERApp(App):
    def build(self):
        return MyGridLayout()

if __name__=="__main__":
    SERApp().run()