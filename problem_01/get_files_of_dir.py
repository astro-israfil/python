import os

# Specify the directory path
folder_path = '/Users/imisr/Downloads'

# Get the list of files and directories in the specified folder
contents = os.listdir(folder_path)

# Print the contents
for item in contents:
    print(item)