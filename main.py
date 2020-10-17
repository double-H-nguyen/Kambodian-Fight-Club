import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from game_logic import Game

p1_selection = 999
p1_sum_selection = 999

p2_selection = 999
p2_sum_selection = 999

game = Game()


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

class P1GuessNumber(Screen):
  def store_p1_num(self, p1_input):
    global p1_selection 
    p1_selection = p1_input
    print_current_state()

class P1GuessSum(Screen):
  def store_p1_sum(self, p1_input):
    global p1_sum_selection
    p1_sum_selection = p1_input
    print_current_state()

class GiveToP2(Screen):
  pass

class Player2Selector(Screen):
  def store_p2_num(self, p2_input):
    global p2_selection
    p2_selection = p2_input
    print_current_state()

class WindowManager(ScreenManager):
  pass

def print_current_state():
  print(f"P1 choice: {p1_selection}")
  print(f"P1 sum: {p1_sum_selection}")
  print(f"P2 choice: {p2_selection}")
  print(f"P2 sum: {p2_sum_selection}")

kv = Builder.load_file("main.kv") 
class Main(App):
  def build(self):
    return kv

if __name__ == "__main__":
  Main().run()
  