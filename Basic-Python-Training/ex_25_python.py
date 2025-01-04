#Topic : BASIC PYTHON
#Exercise Number : 25
##PROBLEM STATEMENT:
#Provide two different solution for below problem:
#Make sure code work on both the windows and linux systems.
# Python Version : 3.7
"""
Python code to list all the files in current directory with all detailed information
i.e. permission, owner, file created and etc. like we have output for ls -l
    - After that convert all the python files in the existing directory to the text files in the same location
    - After updating python files, Move all the python files to some specific folder/ location
    - Make sure your code output must have intuitive logs for the users
NOTE: Use OS module for performing various operations.
"""
import os
current_dir = os.getcwd()
archive_dir = os.path.join(current_dir, "python_files(.py files)")
if not os.path.exists(archive_dir):
    os.makedirs(archive_dir)
for file in os.listdir(current_dir):
    file_path = os.path.join(current_dir, file)
    if os.path.isfile(file_path):
        stats = os.stat(file_path)
        permissions = oct(stats.st_mode)[-3:]
        created_time = datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
        print(f"File: {file} | Permissions: {permissions} | Created: {created_time} | Size: {stats.st_size} bytes")
for file in os.listdir(current_dir):
    if file.endswith(".py"):
        py_file = os.path.join(current_dir, file)
        txt_file = os.path.join(current_dir, file.replace(".py", ".txt"))
        with open(py_file, 'r') as src, open(txt_file, 'w') as dest:
            dest.write(src.read())
        shutil.move(py_file, os.path.join(archive_dir, file))
        print(f"Converted {file} to {file.replace('.py', '.txt')} and moved to archive.")
