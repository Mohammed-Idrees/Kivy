from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    Label:
        canvas.before:
            Color:
                rgba: 1,0,0,0.35
            Rectangle:
                pos: self.pos
                size: self.size
        text: "Title"
        size_hint_y: None
        height: sp(64)
        font_size: sp(56)
    Label:
        canvas.before:
            Color:
                rgba: 0,1,0,0.35
            Rectangle:
                pos: self.pos
                size: self.size
        text: 'Description\\n demo for text'
        text_size: self.size
        valign: 'top'
    Label:
        canvas.before:
            Color:
                rgba: 0,0,1,0.35
            Rectangle:
                pos: self.pos
                size: self.size
        text: 'Footer'
        size_hint_y: None
        height: sp(36)

'''))
