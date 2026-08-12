
import os
import shutil


file_categories = {
    "Images":[".jpg" ,".png" ,".jpeg",".gif",".webp",".svg"],
    "Documents":[".pdf" ,".txt" ,".docx",".doc",".xlsx",".pptx"],
    "Music":[".mp3",".wav",".flac"],
    "Videos":[".mp4",".mkv",".avi",".mov"],
    "Coding_files":[".py",".c",".js",".cpp",".r",".html"],
    "Archives":[".zip",".rar",".7z"]
}


def get_folder_path():
    while True:
     
        path=input("Enter folder path: ")

        try:
         
            file_names=os.listdir(path)
            return path
            

        except FileNotFoundError:
          
            print("Folder not found.")
            print("Please enter a valid folder path.")



def get_file_category(extension):
      category = "Others"

      for category_name in file_categories:
        if extension in file_categories[category_name]:
            category = category_name
            break

      return category

def get_unique_destination(destination_folder, file_name):

    destination = os.path.join(destination_folder, file_name)
    
    if os.path.exists(destination):

        name, extension = os.path.splitext(file_name)
        counter = 1
    
        while os.path.exists(destination):

            new_name = name + "_" + str(counter) + extension
            destination = os.path.join(destination_folder, new_name)
            counter += 1
        
    return  destination

    

def organize_files(path):

    statistics = {
        "Images": 0,
        "Documents": 0,
        "Music": 0,
        "Videos": 0,
        "Python": 0,
        "Others": 0
    }

    file_names = os.listdir(path)

    for file_name in file_names:
        full_path = os.path.join(path, file_name)

        if not os.path.isfile(full_path):
            continue

        _, extension = os.path.splitext(file_name)
        extension = extension.lower()

        category = get_file_category(extension)

        destination_folder = os.path.join(path, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination = get_unique_destination(
            destination_folder,
            file_name
        )

        shutil.move(full_path, destination)
        statistics[category] += 1
        
        print(os.path.basename(destination), "→", category)

    return statistics


def show_statistics(statistics):
     print("\n","-"*40)
     print("         Organization Complete")
     print("-"*40)

     total_files = 0

     for category, count in statistics.items():
        print(f"{category:<12}: {count}")
        total_files += count

     print(f"{'Total files':<12}: {total_files}")


def main():
    path = get_folder_path()
    statistics=organize_files(path)
    show_statistics(statistics)


if __name__ == "__main__":

    main()


    