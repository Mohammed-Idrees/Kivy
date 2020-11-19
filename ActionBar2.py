from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint: {'top': 1}
    ActionView:
        ActionPrevious:
            title: 'Action Bar'
            with_previous: True
        ActionOverflow:
        ActionButton:
            text: 'Button 1'
        ActionButton:
            text: 'Button 2'
        ActionButton:
            text: 'Button 3'
        ActionButton:
            text: 'Button 4'
        ActionButton:
            text: 'Button 5'
        ActionGroup:
            text: 'G1'
            ActionButton:
                text: 'Btn 1'
                icon: 'atlas://data/images/defaulttheme/audio-volume-high'
            ActionButton:
                text: 'Btn 2'
            ActionButton:
                text: 'Btn 3'
    '''))
