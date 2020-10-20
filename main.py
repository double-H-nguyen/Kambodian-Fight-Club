import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Always load .kv file first
Builder.load_file("main.kv")

p1_selection = 999
p1_sum_selection = 999

p2_selection = 999
p2_sum_selection = 999

# add new window classes here
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

class Player1Win(Screen):
  pass

class Player2Win(Screen):
  pass

def print_current_state(): # debugging only
  print(f"P1 choice: {p1_selection}")
  print(f"P1 sum: {p1_sum_selection}")
  print(f"P2 choice: {p2_selection}")
  print(f"P2 sum: {p2_sum_selection}")

class WindowManager(ScreenManager):
  def test_game_logic(self):
    if (p1_selection + p2_selection == p1_sum_selection):
      self.current = 'player1_win'
    else:
      self.current = 'player2_win'

# add screens and their names here
sm = WindowManager()
sm.add_widget(MenuWindow(name='menu'))
sm.add_widget(TutorialWindow(name='tutorial'))
sm.add_widget(P1GuessNumber(name='p1_guess_num'))
sm.add_widget(P1GuessSum(name='p1_guess_sum'))
sm.add_widget(GiveToP2(name='give_to_p2'))
sm.add_widget(Player2Selector(name='p2_select_number'))
sm.add_widget(Player1Win(name='player1_win'))
sm.add_widget(Player2Win(name='player2_win'))

class Main(App):
  def build(self):
    return sm

if __name__ == "__main__":
  Main().run()
  