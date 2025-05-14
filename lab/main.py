from files import File
from lab.utils import delete_directory, list_dir_files, check_if_directory_exists, check_if_file_exists
from utils import create_directory


def main():
    current_dir = "C:\\Users\Юлия\\Pycharm\\system_prog\\lab"

    menu = (f"Вы находитесь в директории: {current_dir}\n"
            "\n"
            "1. Создать новую директорию.\n"
            "2. Удалить директорию.\n"
            "3. Вывести список файлов директории. \n"
            "4. Создать файл в выбранной директории.\n"
            "5. Прочитать файл из выбранной директории.\n"
            "6. Записать данный в файл из выбранной директории.\n"
            "7. Удалить файл из выбранной директории.\n"
            "8. Создать копию файла из выбранной директории.\n"
            "9. Переместить файл в другую директорию.\n"
            "10. Переименовать файл из выбранной директории.\n")

    print(menu)

    action = input("Выберите пункт меню: ")
    if action == '1':
        dir_name = input("Введите имя для новой директории: ")
        create_directory(dir_name)

    elif action == '2':
        dir_name = input("Введите имя директории для удаления: ")
        delete_directory(dir_name)

    elif action == '3':
        dir_name = input("Введите имя директории: ")
        list_dir_files(dir_name)

    elif action == '4':
        dir_name = input("Введите имя директории для создания файла: ")
        file_name = input("Введите имя файла для создания: ")

        res = check_if_directory_exists(dir_name)
        if res:
            file_manager = File(dir_name, file_name)
            file_manager.create_file()
        else:
            print("Такой директории не существует")

    elif action == '5':
        dir_name = input("Введите имя директории, в которой находится файл: ")
        file_name = input("Введите имя файла для чтения: ")

        if not check_if_directory_exists(dir_name):
            print("Такой директории не существует.")
        else:
            # Директория есть — проверяем файл
            if not check_if_file_exists(dir_name, file_name):
                print("Такого файла не существует в заданной директории.")
            elif check_if_file_exists(dir_name, file_name):
                # И директория, и файл существуют
                file_manager = File(dir_name, file_name)
                print(file_manager.read_file())

    elif action == '6':
        dir_name = input("Введите имя директории, в которой находится файл: ")
        file_name = input("Введите имя файла для записи: ")
        # если файла не существовало, то файл с таким названием будет инициализирован

        if not check_if_directory_exists(dir_name):
            print("Такой директории не существует.")
        else:
            file_manager = File(dir_name, file_name)
            data = str(input("Введите строку для записи в файл: "))
            file_manager.write_in_file(data)

    elif action == '7':
        dir_name = input("Введите имя директории, из которой Вы хотите удалить файл: ")
        file_name = input("Введите имя файла для удаления: ")

        if not check_if_directory_exists(dir_name):
            print("Такой директории не существует.")
        else:
            if not check_if_file_exists(dir_name, file_name):
                print("Такого файла не существует в заданной директории.")
            elif check_if_file_exists(dir_name, file_name):
                # И директория, и файл существуют
                file_manager = File(dir_name, file_name)
                file_manager.delete_file()
                print(f"Файл {file_name} был удален.")

    elif action == '8':
        dir_name = input("Введите имя директории, из которой Вы хотите скопировать файл: ")
        file_name = input("Введите имя файла для копирования: ")
        dest_dir = input("Введите имя директории для переноса скопированного файла: ")

        if not check_if_directory_exists(dir_name):
            print("Такой директории не существует.")
        else:
            if not check_if_file_exists(dir_name, file_name):
                print("Такого файла не существует в заданной директории.")
            elif check_if_file_exists(dir_name, file_name):
                file_manager = File(dir_name, file_name)
                file_manager.copy_file(dest_dir)
                print(f"Файл {file_name} был скопирован в директорию {dest_dir}.")

    elif action == '9':
        dir_name = input("Введите имя директории, из которой Вы хотите перенести файл: ")
        file_name = input("Введите имя файла для переноса: ")
        dest_dir = input("Введите имя директории для переноса файла: ")

        if not check_if_directory_exists(dir_name):
            print("Такой директории не существует.")
        else:
            if not check_if_file_exists(dir_name, file_name):
                print("Такого файла не существует в заданной директории.")
            elif check_if_file_exists(dir_name, file_name):
                file_manager = File(dir_name, file_name)
                file_manager.move_file(dest_dir)
                print(f"Файл {file_name} был перемещен в директорию {dest_dir}.")

    elif action == '10':
        dir_name = input("Введите имя директории: ")
        file_name = input("Введите имя файла, который Вы хотите переименовать: ")
        new_name = input("Введите новое имя файла: ")

        if not check_if_directory_exists(dir_name):
            print("Такой директории не существует.")
        else:
            if not check_if_file_exists(dir_name, file_name):
                print("Такого файла не существует в заданной директории.")
            elif check_if_file_exists(dir_name, file_name):
                file_manager = File(dir_name, file_name)
                file_manager.rename_file(new_name)
                print(f"Файл {file_name} был переименован на {new_name}.")


main()
