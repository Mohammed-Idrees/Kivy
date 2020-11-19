from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
FloatLayout:
    Scatter:
        size: 100, 100
        pos: 200, 300
        do_rotation: True
        Label:
            text: 'Scatter'
    '''))


