from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
PageLayout:
    Button:
        text: 'page 1'

    Button: 
        text: 'page 2'

    Button:
        text: 'page 3'
    Button:
        text: 'page 4'

'''))
