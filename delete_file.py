import shutil
import os

def dir_delete(delete_path):
    if os.path.isdir(delete_path):
        shutil.rmtree(delete_path)
    else:
        os.remove(delete_path)

if __name__ == '__main__':
    dir_delete('')