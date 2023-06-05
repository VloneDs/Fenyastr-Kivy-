from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

class MainWidget(BoxLayout):
    oplata_label = ObjectProperty()
    name_input = ObjectProperty()
    image_source = StringProperty()

    def oplata(self):
        self.oplata_label.text = "Феня ушел в тильт (вас заскамили)"
        self.image_source = 'da.png'

    def change_image(self):
        app.root.ids['my_image'].source = 'da.png'
    
class Main(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    app = Main()
    app.run()