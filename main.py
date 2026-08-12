
import os
import shutil

file_categories = {

   "Images":[".jpg" ,".png" ,".jpeg"],
   "Documents":[".pdf" ,".txt" ,".docx"],
   "Music":[".mp3",".wav"],
   "Videos":[".mp4",".mkv"],
   "Python":[".py"],

}

while True:
     
    path=input("Enter folder path: ")

    try:
         
        file_names=os.listdir(path)
        break

    except FileNotFoundError:
          
          print("Folder not found.")
          print("Please enter a valid folder path.")
         


for file_name in file_names:

    full_path = os.path.join(path, file_name)
    if not os.path.isfile(full_path):
        continue

    name,extension=os.path.splitext(file_name)
    extension = extension.lower()
    category = "Others"


    for category_name in file_categories:
            if extension in file_categories[category_name]:
                category = category_name
                break

            
    destination_folder = os.path.join(path, category)
    os.makedirs(destination_folder, exist_ok=True)
    destination = os.path.join(destination_folder, file_name)

    if os.path.exists(destination):
          counter = 1

    while os.path.exists(destination):
        new_name = name + "_" + str(counter) + extension
        destination = os.path.join(destination_folder, new_name)
        counter += 1
    shutil.move(full_path, destination)

    print(file_name, "→", category)

        