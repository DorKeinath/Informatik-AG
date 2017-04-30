#!/usr/bin/env python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class WurzelWidget(BoxLayout):
    pass

class HalloWidgetApp(App):
    def build(self):
        return WurzelWidget()

if __name__ == '__main__':
    HalloWidgetApp().run()
