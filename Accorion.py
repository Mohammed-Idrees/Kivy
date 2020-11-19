from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label

class AccordionApp(App):
    def build(self):
        root = Accordion()
        for x in range(5):
            item = AccordionItem(title = 'Title %d' % x)
            item.add_widget(Label(text = 'Edris\n' *5))
            root.add_widget(item)
        return root

if __name__ == '__main__':
    AccordionApp().run()
