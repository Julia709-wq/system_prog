import os

# получаем от пользователя путь для создания директории
directory = input("Введите путь для создания директории: ")

# проверяем существует такая директория или нет
if os.path.exists(directory):
    print("Директория уже существует")
else:
    os.makedirs(directory)
    print(f"Директория {directory} создана")


def list_files(directory_name):
    for root, dirs, files in os.walk(directory_name):
        for file in files:
            print(os.path.join(root, file))


directory = input("Введите путь к директории для перечисления файлов: ")
list_files(directory)
