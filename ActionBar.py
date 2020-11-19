from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint: {'bottom': 1}
    ActionView:
        ActionPrevious:
            title: 'Action Bar'
            with_previous: True

    '''))
