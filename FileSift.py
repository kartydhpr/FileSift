###############################################################################
# Name: FileSift
# Author: Karteikay Dhuper
# Date: May 17th 2021
# Description This program sifts through all the files in my Downloads folder 
# and redirects them to an approriate folder based on it's filetype. This is 
# done tokeep my Downloads folders free from clutter.
###############################################################################

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# guide used for implementing watchdog: https://pythonhosted.org/watchdog/quickstart.html

import os # to manipulate directories in the file system
import time # to keep track of system tick 
import json # to transmit data

# variable initialization --> stores file path to each type of file
downloads_folder_location = "/Users/karteikaydhuper/Downloads"
music_folder_location = "/Users/karteikaydhuper/Desktop/OrganizedLoads/Music"
video_folder_location = "/Users/karteikaydhuper/Desktop/OrganizedLoads/Videos"
image_folder_location = "/Users/karteikaydhuper/Desktop/OrganizedLoads/Images"
document_folder_location = '/Users/karteikaydhuper/Desktop/OrganizedLoads/Documents'
#trash_folder_location = ""

# lists contain various file extensions for differnet multi-media
image_extensions = ['.png','.PNG','jpeg','.JPG','.jpg','.tif','tiff','.raw','.gif','.eps']
video_extensions = ['.mp4','.MP4','.mov','.MOV','.mkv','.MKV','.srt','.SRT','.avi','.AVI']
music_extensions = ['.m4a','.M4A','.mp3','.MP3','.wav','.WAV','.aac','.AAC']
documents_extensions = ['.doc','DOCX','docx','.pdf','.PDF','ages','.txt','.TXT','.DOC','.ppt','.PPT','.xls','.XLS','xlsx','XLSX']

# event handler class
class File_Handler (FileSystemEventHandler):
    def on_modified (self, event):
        for file in os.listdir(downloads_folder_location):
            origin = downloads_folder_location + '/' + file
            file_extension = file[-4:] # stores the filetype e.g pdf, png, mov, mp4  etc.
            if file_extension in image_extensions:
                destination = image_folder_location + '/' + file # if file is an image, it's destination will be the image folder
            elif file_extension in video_extensions:
                destination = video_folder_location + '/' + file # if file is a video, it's destination will be the video folder
            elif file_extension in music_extensions:
                destination = music_folder_location + '/' + file # if file is music, it's destination will be the music folder
            elif file_extension in documents_extensions:
                destination = document_folder_location + '/' + file # if file is a document, it's destination will be the documentsfolder
            else:
                destination = downloads_folder_location +'/'+ file # if it is a special file then it stays in the Downloads folder
            os.rename(origin, destination) # renames file's filepath to new destination instead of orignal downloads folder

try:
    # mainline running logic
    run_portal = File_Handler() # instance of the File_Handler class stored in "run_portal" variable
    obs = Observer()
    obs.schedule(run_portal, downloads_folder_location, recursive = True)
    obs.start()

    # print statements for "user-interface"
    welcome_message = " ~ Welcome to FileSift™ ~ "
    goodbye_message = " ~ Thank you for using FileSift™! ~ "
    copyright_message = "Copyright © 2021 Karteikay Dhuper. All rights reserved."
    print("\n")
   # print("".center(127,'#'))
    print(f"{welcome_message.center(127,'#')}")
    #print("- By Karteikay Dhuper -".center(127))
    print("\n   1. FileSift organizes the contents of your Downloads folder so you don't have to!")
    print("\n   2. To get started; navigate to your Downloads folder and open a downloaded file -- then let FileSift do the rest!")
    print('\n   3. Watch as FileSift goes through the Downloads folder and organizes similar files in the "OrganizedLoads" folder.')
    print('\n   4. To exit the program press "ctrl + c".')
    print(f"\n{goodbye_message.center(127,'#')}")
    print()
    print(f"\n{copyright_message.center(127)}")

except KeyboardInterrupt:
    obs.stop()
   # print("Program terminated. Thank you for using FileSift")
obs.join()
