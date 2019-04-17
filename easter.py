from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.properties import StringProperty
from random import choice

class EasterScreen(FloatLayout):

    source = StringProperty(None)

    def __init__(self, **kargs):
        super(EasterScreen, self).__init__(**kargs)
        self.image1 = None
        self.image2 = None
        self.image3 = None

    def easter_callback(self):

        possible_choice = [1,2,3]
        chosen = choice(possible_choice)

        if self.image1 != None:
            self.remove_widget(self.image1)
            self.image1 = None

        if self.image2 != None:
            self.remove_widget(self.image2)
            self.image2 = None

        if self.image3 != None:
            self.remove_widget(self.image3)
            self.image3 = None

        if chosen == 1:
            self.source = 'resources/easter_egg_1.png'
        elif chosen == 2:
            self.source = 'resources/easter_egg_2.png'
        else:
            self.source = 'resources/easter_egg_3.png'
        
class EasterApp(App):
    def build(self):
        self.title = "Kabbo's Easter Egg Hunt"
        return EasterScreen()

if __name__ == '__main__':
    EasterApp().run()