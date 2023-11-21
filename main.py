#Импорт библиотек
import ultralytics
from ultralytics import YOLO
import cv2 as cv
import torch

print(torch.cuda.is_available())

#Загрузка модели YOLOv8
model = YOLO('yolov8m-oiv7.pt')

#Обработка фото
def image_processing(image):
    return model.predict(image, show = True)

#Обработка видео
def video_processing(video):
    return model.predict(video, show = True)

