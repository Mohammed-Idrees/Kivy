from kivy.app import App
from kivy.uix.widget import Widget

class test1(Widget):
    def on_touch_down(self,touch):
        print(touch)

class testApp(App):
    def build(self):
        return test1()

if __name__ == '__main__':
    testApp().run()
