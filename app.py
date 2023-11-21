#Импорт []файла
import main
#Импорт библиотек
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout 
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty


#Первый экран
class FirstScreen(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)           
        
        logo = Image(source = 'logo.png')
        label = Label(text='OBJECT DETECTING', color = (0, 0, 0, 1))
        button = Button(text='Начать', 
                        size_hint=(.2, .06), 
                        pos_hint ={'center_x': .5, 'center_y': .2},
                        background_color = (0, 0, 0, 1))
        
        button.on_press = self.next
        
        
        self.add_widget(logo)
        self.add_widget(button)
        
    def next(self):
        self.manager.current = 'second'

#Второй экран
class SecondScreen(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

#Управление приложением
class MyApp(App):
    
    def build(self):
        
        Window.clearcolor = (1, 1, 1, 1)
        self.title = "ObjectDetecting"
        self.icon = 'icon.png'
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm
    
    
if __name__ == '__main__':
    MyApp().run()