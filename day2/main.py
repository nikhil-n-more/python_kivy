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

        #Set Columns
        self.cols = 2

        self.add_widget(Label(text="Name: "))

        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favourite: "))

        self.favourite = TextInput(multiline=False)
        self.add_widget(self.favourite)

        self.add_widget(Label(text="Address: "))

        self.address = TextInput(multiline=True)
        self.add_widget(self.address)

        #Create submit button
        self.submit = Button(text="Submit", font_size=30)
        #Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        favourite = self.favourite.text
        address = self.address.text

        #Print the info to screen
        self.add_widget(Label(text=f'Hello {name} your favourite is {favourite} and your address is {address}'))

        #Clear the input boxes
        self.name = ""
        self.favourite = ""
        self.address = ""

class SERApp(App):
    def build(self):
        return MyGridLayout()

if __name__=="__main__":
    SERApp().run()