import os
def copy_file():
    copyfile = os.path.abspath('copy')
    shutil.copy2(__file__, copyfile)


def files_in_folder():
    for i in os.listdir():
        print(i)


def create_Ndir(n):
    for i in range(1,n):
        try:
            os.mkdir('dir_' + str(i))
        except FileExistsError:
            i += 1

def create_dir(new_name):
    dir_path = os.path.join(os.getcwd(), new_name)
    try:
        os.mkdir(new_name)
        print('Успешно создано!')
    except FileExistsError:
        print('Невозможно создать!')


def remove_dir(n):
    for i in range(1,n):
        os.rmdir('dir_' + str(i))

def delete_dir(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.rmdir(dir_path)
        print('Успешно удален!')
    except:
        print('Невозможно удалить!')

