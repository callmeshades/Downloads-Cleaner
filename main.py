import downloads
from time import sleep

if __name__ == "__main__":
    print("Starting DownloadCleanup V1 by Brandon Nilsson")
    files = downloads.Downloads()
    files.change_to_downloads_folder()
    downloads.create_all_folders()
    files.move_all_files()
    print("Finished moving all files")
    print("Closing in 5 seconds...")
    sleep(5)
