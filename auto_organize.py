#!/usr/bin/env python3
import os
import shutil

def organize_by_extension(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            ext = filename.split('.')[-1]
            target_dir = os.path.join(directory, ext)
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(os.path.join(directory, filename), os.path.join(target_dir, filename))

if __name__ == '__main__':
    dir_to_organize = '.'
    organize_by_extension(dir_to_organize)
    print('Files organized by extension.')
