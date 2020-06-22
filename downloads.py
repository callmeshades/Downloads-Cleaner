import os
import shutil

import config
import os_details


def create_all_folders():
    print('Checking for and creating folders')
    for folder_name in config.folder_names:
        if not os.path.isdir(f'./{folder_name}'):
            os.mkdir(f'./{folder_name}')
            print(f'Created directory: {folder_name}')
        else:
            print(f'Directory {folder_name} already exists, skipping')


class Downloads:
    def __init__(self):
        self.current_user = os_details.fetch_current_user()
        self.platform = os_details.fetch_device_platform()
        self.downloads_folder = self.create_downloads_path()

    def create_downloads_path(self) -> str:
        if 'Windows' in self.platform:
            return f'C:/Users/{self.current_user}/Downloads'
        else:
            print("This platform is not supported at this time.")
            quit()

    def change_to_downloads_folder(self):
        # Check if we're currently in the downloads folder
        # If not change to it
        if os.getcwd() != self.downloads_folder:
            os.chdir(self.downloads_folder)

    def move_all_files(self):
        # Get all files in the current directory
        files = (file for file in os.listdir(self.downloads_folder)
                 if os.path.isfile(os.path.join(self.downloads_folder, file)))
        for file in files:
            self.move_based_on_filetype(file)

    def move_file(self, file, folder):
        shutil.move(f'{self.downloads_folder}/{file}', f'{self.downloads_folder}/{folder}/{file}')

    def move_based_on_filetype(self, file):
        # This type check and moving feature needs to be improved drastically
        # For the time being this will suffice
        file_ext = file.split('.')[-1]
        if file_ext in config.images:
            self.move_file(file, 'Images')
        elif file_ext in config.compressed:
            self.move_file(file, 'Archives')
        elif file_ext in config.audio:
            self.move_file(file, 'Audio')
        elif file_ext in config.disc_and_media:
            self.move_file(file, '')
            self.move_file(file, 'Disc & Media')
        elif file_ext in config.documents:
            self.move_file(file, 'Documents')
        elif file_ext in config.data:
            self.move_file(file, 'Data & Databases')
        elif file_ext in config.emails:
            self.move_file(file, 'Emails')
        elif file_ext in config.executables:
            self.move_file(file, 'Executables')
        elif file_ext in config.fonts:
            self.move_file(file, 'Fonts')
        elif file_ext in config.design:
            self.move_file(file, 'Design')
        elif file_ext in config.java:
            self.move_file(file, 'Java')
        elif file_ext in config.python:
            self.move_file(file, 'Python')
        elif file_ext in config.internet:
            self.move_file(file, 'Internet')
        elif file_ext in config.c_files:
            self.move_file(file, 'C')
        elif file_ext in config.dot_net:
            self.move_file(file, 'DotNet')
        elif file_ext in config.perl:
            self.move_file(file, 'Perl')
        elif file_ext in config.bash:
            self.move_file(file, 'Bash')
        elif file_ext in config.swift:
            self.move_file(file, 'Swift')
        elif file_ext in config.system:
            self.move_file(file, 'System')
        elif file_ext in config.video:
            self.move_file(file, 'Videos')
