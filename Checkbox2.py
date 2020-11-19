from kivy.app import App
from kivy.lang import Builder

kv = """
BoxLayout:
    orientation: 'vertical'
    CheckBox:
        group: 'a'
        active: True
    CheckBox:
        id: Check
        group: 'b'
    Button:
        text: 'yes'
        on_press: Check.active = True
    Button:
        text: 'No'
        on_press: Check.active = False

"""

class testApp(App):
    def build(self):
        return(Builder.load_string(kv))

if __name__ =='__main__':
    testApp().run()
