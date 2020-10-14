import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MenuWindow(Screen):
    pass

class TutorialWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv") 


class Main(App):
  def build(self):
    return kv


if __name__ == "__main__":
  Main().run()