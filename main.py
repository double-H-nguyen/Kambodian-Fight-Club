import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

player1_selection = 999


class MenuWindow(Screen):
    pass

class TutorialWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MenuWindow(Screen):
  pass

class TutorialWindow(Screen):
  pass

class StartGameWindow(Screen):
  def p1_btn_number(self, p1_selection):
    print(f"You pressed the {p1_selection} button (this function was called in main.py)")
    global player1_selection 
    player1_selection = p1_selection
    print_p1_response()

class P1GuessNumber(Screen):
  pass

class WindowManager(ScreenManager):
  pass

def print_p1_response():
  print(f"Player 1's response was {player1_selection}")

kv = Builder.load_file("main.kv") 
class Main(App):
  def build(self):
    return kv

if __name__ == "__main__":
  Main().run()
  