from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


kv="""
AnchorLayout:
    TextInput:
        size_hint: None, None
        size: 400,30
        text: 'Select this text, then maximize the window.'
        use_bubble: True


"""



class test1(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    test1().run()
