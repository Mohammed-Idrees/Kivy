from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
AnchorLayout:
    canvas:
        Color:
            rgb: 1,3,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    AsyncImage:
        size_hint: None, None
        size: dp(56), dp(56)
        source: 'https://github.com/dessant/kivy-designer/releases/download/1/spinner.zip'
        anim_delay: 0.20
    '''))

