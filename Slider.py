from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    padding: 50
    ProgressBar:
        id: bar
        value: Slider.value
        max: 300
    Slider:
        id: Slider
        max: 300
        value: 200
    Slider:
        orientation: 'vertical'
        on_value: Slider.value = self.value
'''))

