import os
import shutil

from_dir = "C:/Users/halanisa/Desktop/Hala/Project 111/Folder"
to_dir = "C:/Users/halanisa/Desktop/Hala/Project 111/Folder2" 


list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(i)
    print(name)
    print(extension)