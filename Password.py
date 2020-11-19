from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

kv = '''
BoxLayout:
    CheckBox:
        id: cd
    TextInput:
        password: True
        multiline: cd.active
'''

runTouchApp(Builder.load_string(kv))
