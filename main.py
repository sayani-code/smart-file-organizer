
import os
import shutil


file_names=os.listdir(input("Enter folder path: "))
print(file_names)
for file_name in file_names:
    name,extention=os.path.splitext(file_name)
    print(name,"     ",extention)