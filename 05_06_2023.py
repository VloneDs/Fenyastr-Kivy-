from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


# Window.clearcolor = (.9, .9, .9, 1)
# class Main(App):
#     def build(self):
#         lable = Label(text='Hello мир, манера крутит мир')
#         return lable
    

# if __name__ == '__main__':
#     app = Main()
#     app.run()
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
    

        # layout = BoxLayout()
        # lable1 = Label(text='Hello мир ')
        # lable2 = Label(text='!')
        # lable3 = Label(text='Mанера крутит мир')
        # layout.add_widget(lable1)
        # layout.add_widget(lable2)
        # layout.add_widget(lable3)
        # return layout
    

if __name__ == '__main__':
    app = Main()
    app.run()