from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.image import AsyncImage

Builder.load_string('''
<CenteredAsyncImage>:
    size: self.texture_size
    size_hint: None, None
    pos_hint: {'center_x':0.5, 'center_y': 0.5}

''')

class centeredAsyncImage(AsyncImage):
    pass

class testimage(App):
    def build(self):
        return centeredAsyncImage(source='http://kivy.org/funny-pictures-cat-is-expecting-you.jpg')

if __name__ == '__main__':
    testimage().run()

