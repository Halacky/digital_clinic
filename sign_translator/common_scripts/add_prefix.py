import os

def add_prefix_to_files(folder_path):
    # Получаем название папки
    folder_name = os.path.basename(os.path.normpath(folder_path))

    # Перебираем все файлы в папке
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Проверяем, что это файл (а не папка)
        if os.path.isfile(file_path):
            # Новый путь с добавленным префиксом
            new_file_name = f"{folder_name}_{file_name}"
            new_file_path = os.path.join(folder_path, new_file_name)

            # Переименовываем файл
            os.rename(file_path, new_file_path)
            print(f"Переименован: {file_name} -> {new_file_name}")

if __name__ == "__main__":
    # Укажите путь к папке
    folder_path = input("Введите путь к папке: ").strip()

    if os.path.isdir(folder_path):
        add_prefix_to_files(folder_path)
        print("Все файлы обновлены.")
    else:
        print("Указанный путь не является папкой.")
