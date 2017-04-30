# http://stackoverflow.com/questions/43705206/kivy-wrong-on-release-on-press-or-widget-access-from-second-click-on

#!/usr/bin/env python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class Login(BoxLayout):
    outpt = StringProperty()

    def access_widget_1(self,inpt_name):
        self.outpt = 'Your name is : ' + inpt_name

    def access_widget_2(self,inpt_pwd):
        self.ids["outputlabel"].text = 'Your password is: ' + inpt_pwd

class WidgetAccessApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    WidgetAccessApp().run()

# widgetaccess.kv
# <Login>:
#     outpt: outpt
#
#     BoxLayout:
#         orientation: 'vertical'
#
#         TextInput:
#             id: inpt_name
#
#         TextInput:
#             id: inpt_pwd
#
#         Button:
#             text: "Run!"
#             on_press: root.access_widget_1(inpt_name.text)
#             on_release: root.access_widget_2(inpt_pwd.text)
#
#         Label:
#             id: outputlabel
#             text: root.outpt
