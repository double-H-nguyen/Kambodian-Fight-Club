import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 1, 0, .5, mode='rgba')
            Line(points = (0, 0, 150, 150, 270, 0, 212, 73, 68, 73))
            Color(1, 0, 0, .5, mode='rgba')
            self.rect = Rectangle(pos=(0,0), size=(50, 50))

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse down", touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse move", touch)

    def on_touch_up(self, touch):
        print("Mouse Up", touch)

class KivyTutorial8(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    KivyTutorial8().run()
