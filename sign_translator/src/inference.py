import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO

def load_frames_from_folder(folder_path):
    """Загружает все изображения из указанной папки."""
    frames = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        frames.append(file_path)
    return frames

def draw_predictions_on_frame(frame_path, predictions):
    """Отображает результаты предсказаний на кадре."""
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for pred in predictions:
        class_id = int(predictions.top1)  # Класс
        score = predictions.top1conf.item()  # Уверенность

        # Добавим текст с названием класса и вероятностью
        text_coord = (30, 50)
        frame = cv2.imread(frame_path)
        gr_tr = frame_path.split("\\")[-1].split("_")[0]
        label = f"Predict {labels[class_id]}, Truth {gr_tr}, score {score:.2f}"
        
        cv2.putText(frame, label, text_coord, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
    cv2.imwrite(f'Pictures/{labels[class_id]}_{score:.2f}.png', frame)
    return frame

def main():
    # Путь к папке с изображениями
    folder_path = "Pictures/test_images"

    # Загружаем модель YOLOv8
    model = YOLO("Downloads/best.pt")

    # Загружаем кадры
    frames = load_frames_from_folder(folder_path)
    if not frames:
        print("Не удалось загрузить кадры из папки.")
        return

    # Список кадров с предсказаниями
    frames_with_predictions = []

    # Обрабатываем каждый кадр
    for frame in frames:
        results = model(frame)  # Получаем предсказания
        print(results[0].probs)
        annotated_frame = draw_predictions_on_frame(frame, results[0].probs)
        frames_with_predictions.append(annotated_frame)


main()