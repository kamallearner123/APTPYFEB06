
# Write a function to collect all .py files from Templates directory and copy to all other directories in Assignments directory.
# The function should take no arguments and return None.
# The function should use the shutil module to copy files.
# The function should use the os module to list files and directories.
# The function should use the os.path module to join paths.
# The function should use the os.path module to check if a path is a file.
# The function should use the os.path module to check if a path is a directory.
# The function should use the os.path module to check if a path exists.
# The function should use the os.path module to check if a path is a symbolic link.


import os
import shutil

# Copy all the files recursively from Templates directory to all other directories in Assignments directory
def copy_files():
    # Get the current directory
    current_dir = os.getcwd()

    # Get the Templates directory
    templates_dir = os.path.join(current_dir, "Templates")

    # Get the Assignments directory
    assignments_dir = os.path.join(current_dir, "./")

    # Get all the files in the Templates directory
    files = os.listdir(templates_dir)
    print(files)

    # Copy all the files to all other directories in Assignments directory
    for file in files:
        dir_path = os.path.join(templates_dir, file)
        # go through all the directories in Assignments directory
        for dir in os.listdir(assignments_dir):
            # check if the path is a directory
            if os.path.isdir(os.path.join(assignments_dir, dir)):
                # check if the path exists
                if os.path.exists(os.path.join(assignments_dir, dir)):
                    # check if the path is a symbolic link
                    if not os.path.islink(os.path.join(assignments_dir, dir)):
                        # copy the file to the directory
                        shutil.copy(dir_path, os.path.join(assignments_dir, dir))


if __name__ == '__main__':
    copy_files()