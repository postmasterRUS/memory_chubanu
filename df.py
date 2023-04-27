from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

#sdgfgjhjkl
class ScrButton(Button):
  def __init__(self, screen, direction='right', goal='main', **kwargs):
      super().__init__(**kwargs)
      self.screen = screen
      self.direction = direction
      self.goal = goal
  def on_press(self):
      self.screen.manager.transition.direction = self.direction
      self.screen.manager.current = self.goal

class MainScr(Screen):
  def __init__(self, **kwargs):
      super().__init__(**kwargs)
      vl = BoxLayout(orientation='vertical', padding=8, spacing=2)
      hl = BoxLayout()
      txt = Label(text= 'Выбери экран')
      b1=ScrButton(self,direction='up',goal='first',text='1')
      b2=ScrButton(self,direction='right',goal='second', text='2')
      b3=ScrButton(self,direction='down',goal='third', text='3')
      b4=ScrButton(self,direction='left',goal='fourth',text='4')
      vl.add_widget(b1)
      vl.add_widget(b2)
      vl.add_widget(b3)
      vl.add_widget(b4)
      hl.add_widget(txt)
      hl.add_widget(vl)
      self.add_widget(hl)

class First(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        hl = BoxLayout(orientation='vertical', size_hint=(.3, .3), 
        pos_hint={'center_x': 0.5, 'center_y': 0.5})

        b1=Button(text='Просто кнопка',size_hint=(.5, 1), 
        pos_hint={'left': 0})
        b_back=ScrButton(self,direction='right', goal='main',text='на главный экран',
         size_hint=(.5, 1), pos_hint={'right': 1})
        hl.add_widget(b1)
        hl.add_widget(b_back)
        self.add_widget(hl)

class MyApp(App):
  def build(self):
      sm = ScreenManager()
      sm.add_widget(MainScr(name='main'))
      sm.add_widget(First(name='first'))

      
      return sm

MyApp().run()




