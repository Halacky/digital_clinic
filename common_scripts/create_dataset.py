import os
import shutil
import random

# Исходная папка с изображениями
source_folder = "/home/kirill/Desktop/eng/images"  # Укажите путь к папке с изображениями

dataset_folder = "/home/kirill/project/digital_clinic/eng_alphabet"  # Папка для нового датасета
train_folder = os.path.join(dataset_folder, "train")
test_folder = os.path.join(dataset_folder, "test")

# Создать папки train и test
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Собираем все файлы из исходной папки
all_images = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# Перемешиваем изображения
random.shuffle(all_images)

# Создаем словарь для хранения классов
class_images = {}
for image in all_images:
    class_name = image[0].lower()  # Первая буква имени файла (в нижнем регистре)
    if class_name not in class_images:
        class_images[class_name] = []
    class_images[class_name].append(image)

# Разделяем изображения на train и test (например, 80% train и 20% test)
split_ratio = 0.8
for class_name, images in class_images.items():
    # Создаем папки для каждого класса
    train_class_folder = os.path.join(train_folder, class_name)
    test_class_folder = os.path.join(test_folder, class_name)
    os.makedirs(train_class_folder, exist_ok=True)
    os.makedirs(test_class_folder, exist_ok=True)

    # Разделяем изображения
    split_index = int(len(images) * split_ratio)
    train_images = images[:split_index]
    test_images = images[split_index:]

    # Копируем изображения в соответствующие папки
    for i, image in enumerate(train_images, 1):
        src_path = os.path.join(source_folder, image)
        dst_path = os.path.join(train_class_folder, f"{class_name}_{i}.png")
        shutil.copy2(src_path, dst_path)

    for i, image in enumerate(test_images, 1):
        src_path = os.path.join(source_folder, image)
        dst_path = os.path.join(test_class_folder, f"{class_name}_{i}.png")
        shutil.copy2(src_path, dst_path)

print("Датасет успешно создан в папке", dataset_folder)