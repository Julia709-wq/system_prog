import os

def check_if_directory_exists(directory_name):
    res = True
    if not os.path.exists(directory_name):
        res = False
    return res

def check_if_file_exists(directory_name, filename):
    file_path = os.path.join(directory_name, filename)
    return os.path.isfile(file_path)

def create_directory(directory_name):
    try:
        os.makedirs(directory_name)
        print(f"Директория {directory_name} создана")
    except FileExistsError:
        print("Директория с таким именем уже существует.")

def delete_directory(dir_name):
    if not os.path.exists(dir_name):
        print("Такой директории не существует")
    try:
        os.rmdir(dir_name)
        print(f"Директория {dir_name} удалена.")
    except OSError as e:
        print("Директория не может быть удалена.", e)

def list_dir_files(dir_name):
    try:
        files = os.listdir(dir_name)
        print("Файлы директории: \n")
        print(files)
    except FileNotFoundError:
        print("Такой директории не существует.")