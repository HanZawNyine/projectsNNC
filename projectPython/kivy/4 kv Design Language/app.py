from kivy.app import App
from kivy.uix.widget import Widget

class myGrid(Widget):
    pass


class myApp(App):
    def build(self):
        return myGrid()


if __name__ == '__main__':
    myApp().run()
