from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class myGrid(Widget):
    firstName = ObjectProperty(None)
    lastName = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print(self.firstName.text, self.lastName.text,self.email.text)
        self.firstName.text =''
        self.lastName.text=''
        self.email.text = ''

class myApp(App):
    def build(self):
        return myGrid()


if __name__ == '__main__':
    myApp().run()
