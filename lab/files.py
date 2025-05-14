import os
import shutil

class File:

    def __init__(self, dir_name, filename):
        self.directory = dir_name
        self.filename = filename
        os.chdir(dir_name)

    def create_file(self):
        open(self.filename, 'w')
        print(f"Файл {self.filename} создан")

    def read_file(self):
        with open(self.filename, 'r') as f:
            data = f.read()
            return data

    def write_in_file(self, data):
        filename = f'C:{self.filename}'
        with open(filename, 'w') as f:
            f.write(data)

    def delete_file(self):
        os.remove(self.filename)

    def copy_file(self, new_dir_name):
        shutil.copy2(self.filename, new_dir_name)

    def move_file(self, new_dir_name):
        shutil.move(self.filename, new_dir_name)


    def rename_file(self, new_name):
        name = str(self.filename)
        os.rename(name, new_name)

