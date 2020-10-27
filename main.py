import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle

#############################################
# KV FILE(S)
# Always load .kv file first
#############################################
Builder.load_file("main.kv")


#############################################
# GLOBAL VARIABLES
#############################################
p1_selection = 999
p1_sum_selection = 999

p2_selection = 999
p2_sum_selection = 999


#############################################
# ADD SCREEN CLASSES
# add new screen/window classes here
#############################################
class MenuWindow(Screen):
  pass

class TutorialWindow(Screen):
  pass

class P1Num1(Screen):
  pass

class P2Num1(Screen):
  pass

class P1Num2(Screen):
  pass

class P2Num2(Screen):
  pass

class P1Sum(Screen):
  pass

class P2Sum(Screen):
  pass

class GiveToP1(Screen):
  pass

class GiveToP2(Screen):
  pass

class DisplayResults1(Screen):
  chosen_number_label = ObjectProperty(None)
  sum = ObjectProperty(None)

  def on_enter(self, *args):
    global p1_selection, p2_selection, p1_sum_selection
    total = p1_selection + p2_selection
    self.chosen_number_label.text = f"Numbers chosen: P1={str(p1_selection)} P2={str(p2_selection)} \n P1 guessed that the sum is: {p1_sum_selection}"
    self.sum.text = f"The sum is: {str(total)}"

class DisplayResults2(Screen):
  chosen_number_label = ObjectProperty(None)
  sum = ObjectProperty(None)

  def on_enter(self, *args):
    global p1_selection, p2_selection, p2_sum_selection
    total = p1_selection + p2_selection
    self.chosen_number_label.text = f"Numbers chosen: P1={str(p1_selection)} P2={str(p2_selection)} \n P2 guessed that the sum is: {p2_sum_selection}"
    self.sum.text = f"The sum is: {str(total)}"

class P1Win(Screen):
  pass

class P2Win(Screen):
  pass

#############################################
# GAME LOGIC (app.root class)
#############################################
class Game(ScreenManager):
  def store_p1_num(self, p1_input):
    global p1_selection 
    p1_selection = p1_input
    print_current_state()

  def store_p2_num(self, p2_input):
    global p2_selection
    p2_selection = p2_input
    print_current_state()

  def store_p1_sum(self, p1_input):
    global p1_sum_selection
    p1_sum_selection = p1_input
    print_current_state()

  def store_p2_sum(self, p2_input):
    global p2_sum_selection
    p2_sum_selection = p2_input
    print_current_state()

  def did_p1_win(self):
    global p1_selection, p2_selection, p1_sum_selection
    if (p1_selection + p2_selection == p1_sum_selection):
      self.current = 'p1_win'
    else:
      self.current = 'p2_num_2'

  def did_p2_win(self):
    global p1_selection, p2_selection, p2_sum_selection
    if (p1_selection + p2_selection == p2_sum_selection):
      self.current = 'p2_win'
    else:
      self.current = 'p1_num_1'


#############################################
# ADD SCREENS
# add screens and their names here
#############################################
g = Game()
g.add_widget(MenuWindow(name='menu'))
g.add_widget(TutorialWindow(name='tutorial'))
g.add_widget(P1Num1(name='p1_num_1'))
g.add_widget(P2Num1(name='p2_num_1'))
g.add_widget(P1Num2(name='p1_num_2'))
g.add_widget(P2Num2(name='p2_num_2'))
g.add_widget(P1Sum(name='p1_sum'))
g.add_widget(P2Sum(name='p2_sum'))
g.add_widget(GiveToP1(name='give_to_p1'))
g.add_widget(GiveToP2(name='give_to_p2'))
g.add_widget(DisplayResults1(name='display_results_1'))
g.add_widget(DisplayResults2(name='display_results_2'))
g.add_widget(P1Win(name='p1_win'))
g.add_widget(P2Win(name='p2_win'))
#g.current='p2_guess_sum'


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
  