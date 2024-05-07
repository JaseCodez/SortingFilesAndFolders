"""
Authors: Jason Phan
Updated: 6th May 24'

Organize files and folders alphabetically
"""

import os
import shutil


class FileOrganizer:

    directory: str
    map: dict[str, list[str]]

    def __init__(self, directory: str) -> None:
        self.directory = directory
        self.map = {}

        for item in os.listdir(self.directory):
            self.map.setdefault(item[0].upper(), []).append(item)

    def organize_files(self) -> None:
        self._create_folder()
        for key, values in self.map.items():
            for value in values:
                src = os.path.join(self.directory, value)
                if not os.path.isdir(src):
                    dst = os.path.join(self.directory, key) + '\\'
                    try:
                        shutil.move(src=src, dst=dst)
                    except shutil.Error:
                        print(f'{value} could not be moved')

    def organize_folders(self) -> None:
        self._create_folder()
        self._create_folder()
        for key, values in self.map.items():
            for value in values:
                src = os.path.join(self.directory, value)
                if os.path.isdir(src):
                    dst = os.path.join(self.directory, key) + '\\'
                    try:
                        shutil.move(src=src, dst=dst)
                    except shutil.Error:
                        print(f'{value} could not be moved')

    def organize(self):
        self.organize_files(), self.organize_folders()

    def organize_new_path(self, directory) -> None:
        self.directory = directory

    def _create_folder(self) -> None:
        for key in self.map.keys():
            path = os.path.join(self.directory, key)
            if not os.path.isdir(path):
                os.mkdir(path)
