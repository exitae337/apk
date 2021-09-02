from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
import geocoder


from kivy.uix.boxlayout import BoxLayout

__version__ = '0.0.1'
Window.clearcolor = (0, .54, .54, .45)

class Nishia(App):
    def updateLabel(self):
        self.lbl.text = self.coord

    def position(self, instance):
        g = geocoder.ip('me')
        self.coord = str(g.latlng)
        self.updateLabel()

    def build(self):
        self.coord = ''
        self.lbl = Label(text="")
        bl = BoxLayout(orientation='vertical')
        bl.add_widget(Label(text="Hello cutie :3", font_size=40, size_hint=(1, .2)))
        al = BoxLayout(orientation='vertical', padding=[200, 5, 200, 5], spacing=5, size_hint=(1, .8))
        al.add_widget(Button(text="WHERE are you :3 ?", on_press=self.position))
        al.add_widget(self.lbl)
        bl.add_widget(al)
        return bl


Nishia().run()
