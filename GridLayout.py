from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
import kivy

Builder.load_string('''
<Demo>:
    cols: 2
    BoxLayout:
        orientation: 'horizontal'
        Button: 
            text: 'Demo'
            pos_hint: {'x': 0}
        Button:
            text: 'Demo'
            pos_hint: {'x': 0}

''')

class Demo(GridLayout):
    pass

class DemoApp(App):
    def build(self):
        return Demo()

if __name__ == '__main__':
    DemoApp().run()
