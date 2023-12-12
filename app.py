#Импорт []файла
import main
#Импорт библиотек
import os
import cv2
from ultralytics import YOLO
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout 
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock

#Загрузка модели YOLOv8
model = YOLO('yolov8m-oiv7.pt')

#Первый экран
class FirstScreen(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)           
        
        logo = Image(source = 'logo.png')
        label = Label(text='OBJECT DETECTING', color = (0, 0, 0, 1))
        version = Label(text="Версия 1.0", 
                        color = (1, 1, 1, 1), 
                        pos_hint ={'center_x': .92, 'center_y': .05})
        button = Button(text='Начать', 
                        size_hint=(.2, .06), 
                        pos_hint ={'center_x': .5, 'center_y': .2},
                        background_color = (0, 0, 0, 1))
        
        button.on_press = self.next
             
        self.add_widget(logo)
        self.add_widget(button)
        self.add_widget(version)

    #Обработка нажатий
    def next(self):
        self.manager.current = 'second'


#Второй экран
class SecondScreen(Screen, Image):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30)       
        
        self.button = Button(text = "Фото", 
                        size_hint=(.2, .06), 
                        pos_hint ={'center_x': .5, 'center_y': .05},
                        background_color = (0, 0, 0, 1)) 
        
        self.button.bind(on_press=self.take_pic)
        
        self.add_widget(self.button)
    
    #Вывод видео   
    def update(self, dt):
        
        ret, self.frame = self.capture.read()
        
        buf = cv2.flip(self.frame, 0).tostring()
        texture = Texture.create(size=(self.frame.shape[1], self.frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        
        self.texture = texture
    
    #Обработка нажатий
    def take_pic(self, *args):
        cv2.imwrite("test.png", self.frame)
        self.manager.current = 'third'
  
        
#Третий экран     
class ThirdScreen(Screen):
    
    def init(self, **kwargs):
        super().init(**kwargs)
        
        button = Button(background_normal = 'back.png', 
                        size_hint=(.05, .05), 
                        pos_hint ={'center_x': .5, 'center_y': .5})
        
        model.predict('test.png', show = True, save = False)
        
        processed_image = Image(source = 'runs/detect/predict/test.png')
    
        button.on_press = self.next

        self.add_widget(processed_image)
        self.add_widget(button)
        
        if os.path.isfile('runs/detect/predict/test.png'): os.remove('runs/detect/predict/test.png')
    
    #Обработка нажатий
    def next(self):
        self.manager.current = 'second'
        
        
#Управление приложением
class MyApp(App):
    
    def build(self):
        
        Window.clearcolor = (1, 1, 1, 1)
        self.title = "ObjectDetecting"
        self.icon = 'icon.png'
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        return sm
    
    
if __name__ == '__main__':
    MyApp().run()