import os
import shutil


class FileOrganizer:
    def __init__(self, directory: str):
        self.directory = directory
        self.map = {}

        for item in os.listdir(self.directory):
            self.map.setdefault(item[0].upper(), []).append(item)

    def organize_files(self):
        self._create_folder()
        for key, values in self.map.items():
            for value in values:
                if '.' in value:
                    dst = os.path.join(self.directory, key) + '\\'
                    src = os.path.join(self.directory, value)
                    shutil.move(src=src, dst=dst)

    def organize_folders(self):
        self._create_folder()
        self._create_folder()
        for key, values in self.map.items():
            for value in values:
                if '.' not in value:
                    dst = os.path.join(self.directory, key) + '\\'
                    src = os.path.join(self.directory, value)
                    shutil.move(src=src, dst=dst)

    def organize(self):
        self.organize_files(), self.organize_folders()

    def _create_folder(self):
        for key in self.map.keys():
            path = os.path.join(self.directory, key)
            if not os.path.isdir(path):
                os.mkdir(path)
