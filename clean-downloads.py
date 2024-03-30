import os
import shutil
from datetime import datetime, timedelta

# set the path of the folder to check
folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# set the path of the folder to move files to
to_delete_folder_path = os.path.join(os.path.expanduser('~'), 'to_delete')

# create the folder if it doesn't exist
if not os.path.exists(to_delete_folder_path):
    os.makedirs(to_delete_folder_path)

# get the list of files in the folder
files = os.listdir(folder_path)

# get the current date
now = datetime.now()

# loop through the files
for file in files:
    # get the file path
    file_path = os.path.join(folder_path, file)

    # get the file's modification date
    modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))

    # calculate the time difference
    time_difference = now - modified_date

    # if the file is older than 30 days, move it
    if time_difference > timedelta(days=30):
        shutil.move(file_path, to_delete_folder_path)