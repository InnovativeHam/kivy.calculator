from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CalScreen(GridLayout):
               def Calculate(self, calculation):
                              if calculation:
                                             try:
                                                            self.display.text = str(eval(calculation))
                                             except Exception:
                                                            self.display.text = "Syntax error"
                              
                              

presentation = Builder.load_file("main.kv")

class Calculator(App):
               def build(self):
                              return presentation

if __name__ == "__main__":
               Calculator().run()
