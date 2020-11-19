from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.app import App


runTouchApp(Builder.load_string('''
StackLayout:
    Button:
        text: 'kivy'
        size_hint: .2,.2
'''))
