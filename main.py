import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

#############################################
# KV FILE(S)
# Always load .kv file first
#############################################
Builder.load_file("main.kv")


#############################################
# GLOBAL VARIABLES
#############################################
p1_selection = 999
p2_selection = 999

p1_sum_selection = 999
p2_sum_selection = 999

p1_turn = 1
p2_turn = 0


#############################################
# ADD SCREEN CLASSES
# add new screen/window classes here
#############################################
class MenuWindow(Screen):
  pass

class TutorialWindow(Screen):
  pass

class P1GuessNumber(Screen):
  pass

class P1GuessSum(Screen):
  pass

class GiveToP1(Screen):
  pass

class GiveToP2(Screen):
  pass

class Player2Selector(Screen):
  pass

class Player1Win(Screen):
  pass

class Player2Win(Screen):
  pass

class ChosenNumber(Screen):
  chosen_number_label = ObjectProperty(None)
  sum = ObjectProperty(None)
  def on_pre_enter(self, *args):
    global p1_selection, p2_selection, p1_sum_selection
    total = p1_selection + p2_selection
    self.chosen_number_label.text = f"Numbers chosen: P1={str(p1_selection)} P2={str(p2_selection)}"
    self.sum.text = f"The Sum is: {str(total)}"

class P2GuessSum(Screen):
  pass

#############################################
# GAME LOGIC (app.root class)
#############################################
class Game(ScreenManager):
  def store_p1_num(self, p1_input):
    global p1_selection 
    p1_selection = p1_input
    print_current_state()

  def store_p1_sum(self, p1_input):
    global p1_sum_selection
    p1_sum_selection = p1_input
    self.current = 'give_to_p2'
    print_current_state()

  def store_p2_num(self, p2_input):
    global p2_selection
    p2_selection = p2_input
    print_current_state()

  def store_p2_sum(self, p2_input):
    global p2_sum_selection
    p2_sum_selection = p2_input
    self.current = 'give_to_p1'
    print_current_state()

  def check_sum():
    pass
  
  def check_if_p1_won():
    pass

  def check_if_p2_won():
    pass

  def test_game_logic(self):
    if (p1_selection + p2_selection == p1_sum_selection):
      self.current = 'player1_win'
    else:
      self.current = 'player2_win'


#############################################
# ADD SCREENS
# add screens and their names here
#############################################
g = Game()
g.add_widget(MenuWindow(name='menu'))
g.add_widget(TutorialWindow(name='tutorial'))
g.add_widget(P1GuessNumber(name='p1_guess_num'))
g.add_widget(P1GuessSum(name='p1_guess_sum'))
g.add_widget(P2GuessSum(name='p2_guess_sum'))
g.add_widget(GiveToP1(name='give_to_p1'))
g.add_widget(GiveToP2(name='give_to_p2'))
g.add_widget(Player2Selector(name='p2_select_number'))
g.add_widget(Player1Win(name='player1_win'))
g.add_widget(Player2Win(name='player2_win'))
g.add_widget(ChosenNumber(name='chosen_number'))
# g.current='chosen_number'


#############################################
# HELPER METHODS
#############################################
def print_current_state(): # debugging only
  print(f"P1 choice: {p1_selection}, P1 sum: {p1_sum_selection}, P2 choice: {p2_selection}, P2 sum: {p2_sum_selection}")

#############################################
# STANDARD CODE
#############################################
class Main(App):
  def build(self):
    return g

if __name__ == "__main__":
  Main().run()
  