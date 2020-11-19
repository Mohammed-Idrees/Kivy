from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
BoxLayout:
    size_hint_x: .7
    size_hint_y: None
    height: sp(150)
    Label:
        text: 'A CheckBox'
'''))

