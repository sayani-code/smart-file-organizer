
import os
import shutil

file_categories = {

   "Images":[".jpg" ,".png" ,".jpeg"],
   "Documents":[".pdf" ,".txt" ,".docx"],
   "Music":[".mp3",".wav"],
   "Videos":[".mp4",".mkv"],
   "Python":[".py"],

}

path=input("Enter folder path: ")
file_names=os.listdir(path)

for file_name in file_names:

    name,extension=os.path.splitext(file_name)
    category_found = False

    for category in file_categories:
            if extension in file_categories[category]:
                category_found = True
            

    if not category_found:
        category = "Others"
        print(file_name, "→", category)