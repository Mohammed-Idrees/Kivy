from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.spinner import Spinner

spinner = Spinner(
    text = 'Home',
    values = ('Home', 'Work', 'Other', 'Word'),
    size_hint = (None, None), Size = (100,44),
    pos_hint = {'center_x': .5, 'center_y': .5}

)

def show_selected_value(spinner, text):
    print('the spinner', spinner, 'have text',text)


spinner.bind(text = show_selected_value)
runTouchApp(spinner)

