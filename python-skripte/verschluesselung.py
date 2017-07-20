#!/usr/bin/env python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
# from kivy.core.window import Window

class Verschluesselung(BoxLayout):
    ausgabe = StringProperty('Es ist noch kein Text zum Übersitzen eingegeben.')

    def verschluessle(self,eingabe):
        self.ausgabe = 'Dein Text ist:\n' + eingabe + '\nRichtig?!'

class VerschluesselungsappApp(App):
    def build(self):
        kivy.Config.set('graphics', 'width',  900)
        kivy.Config.set('graphics', 'height', 600)
        # Window.fullscreen = True
        return Verschluesselung()

if __name__ == '__main__':
    VerschluesselungsappApp().run()
