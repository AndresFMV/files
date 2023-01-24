__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile


def clean_cache():
    global cache_directory
    cache_directory = os.path.join(os.getcwd(), 'files/cache')
    os.makedirs(cache_directory, exist_ok=True)
    if os.path.exists(cache_directory):
        for item in os.scandir(cache_directory):
            if item.is_file():
                os.remove(item.path)


def cache_zip(zip_file_path: str, cache_dir_path: str) -> None:
    cache_dir_path = cache_directory
    zip_file_path = os.path.join(os.getcwd(), 'files/data.zip')
    with ZipFile(zip_file_path, 'r') as z_object:
        z_object.extractall(cache_dir_path)


def cached_files():
    global absolute_path_files
    absolute_path_files = []
    for f in os.listdir(cache_directory):
        if os.path.isfile(os.path.join(cache_directory, f)):
            absolute_path = os.path.abspath(os.path.join(cache_directory, f))
            absolute_path_files.append(absolute_path)
    return absolute_path_files


def find_password(absolute_path_files):
    password_keyword = 'password:'
    for files in absolute_path_files:
        with open(files, 'r') as f:
            for line in f:
                if password_keyword in line:
                    index = line.index(password_keyword)
                    substring = line[index + len(password_keyword):].strip()
                    return substring
