from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
AnchorLayout:
    anchor_x: 'left'
    anchor_y: 'center'
    Button:
        text: 'A1'
        size_hint: .5, .5

    Button: 
        text: 'A2'
        size_hint: .2, .2

'''))
