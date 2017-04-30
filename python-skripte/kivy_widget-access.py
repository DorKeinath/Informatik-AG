#!/usr/bin/env python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class Login(BoxLayout):
    outpt = StringProperty('Fülle bitte beide Felder aus.') # 1. Weg: Um durch access_widget_1 den text des Labels zu ändern, wird hier eine Variable definiert, auf die der Python- und Kivy-Code dieser Klasse ("Plugin") Zugriff haben.

    def access_widget_1(self,inpt_name,inpt_pwd):
        print('Dein Name ist: {x}'.format(x = inpt_name)) # Erste Möglichkeit etwas Übergebenes im Terminal auszugeben.
        print('Dein Passwort ist: ' + inpt_pwd) # Zweite Möglichkeit etwas Übergebenes im Terminal auszugeben.
        self.outpt = 'Dein Name ist: ' + inpt_name

    def access_widget_2(self,inpt_pwd):
        self.ids["ausgabelabel"].text = 'Dein Passwort ist: ' + inpt_pwd # 2. Weg: Wenn man im Kivy-Code dem Label eine id gegeben hat, kann man auf sie zugreifen. Dieser Weg ist praktisch, aber als "best practice" wird der erste Weg angesehen. Der Vorteil ist hier, dass man im Kivy-Code sehen kann, was im Label-Text ausgegeben wird.

class WidgetAccessApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    WidgetAccessApp().run()
