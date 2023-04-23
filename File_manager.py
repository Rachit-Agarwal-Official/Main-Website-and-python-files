import os

# Set the directory path to the folder you want to manage
directory = '/path/to/folder'

# Loop through all files in the directory
for filename in os.listdir(directory):

    # Set the full path to the file
    file_path = os.path.join(directory, filename)

    # Check if the file is a directory or a file
    if os.path.isdir(file_path):
        # If it's a directory, do something
        print('Directory:', file_path)
    else:
        # If it's a file, do something else
        print('File:', file_path)

        # Example file management tasks:
        # Rename the file
        new_filename = filename.replace('old', 'new')
        os.rename(file_path, os.path.join(directory, new_filename))
        
        # Move the file to a different directory
        new_directory = '/path/to/new/folder'
        os.rename(file_path, os.path.join(new_directory, new_filename))
        
        # Delete the file
        os.remove(file_path)