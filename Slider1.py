from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
Slider:
    min: -100
    max: 100
    value: -100
    id: pos_Slider

'''))

