import os
import shutil

def organize_folder(folder_path):

    for file in os.listdir(folder_path):
        old_location = os.path.join(folder_path, file)

        if os.path.isfile(old_location):
                name, exten = os.path.splitext(file)

                if exten in [".jpg", ".png"]:
                     dest_folder_name = "Images"
                elif exten in [".pdf", ".txt", ".docx"]:
                     dest_folder_name = "Documents"
                elif exten in [".mkv", ".mp4"]:
                     dest_folder_name = "Videos"
                elif exten in [".wav", ".mp3"]:
                    dest_folder_name = "Audio"    
                else:
                     dest_folder_name = "Misc"

                dest_folder_path = os.path.join(folder_path, dest_folder_name)

                os.makedirs(dest_folder_path, exist_ok=True)

                new_file_location = os.path.join(dest_folder_path, file)

                shutil.move(old_location, new_file_location)
                print(f"MOved {file} to {dest_folder_name}")


def main():
     while True:
        user = input("Enter folder path: ")

        if user.lower() == 'q':
            print("Thanks for using Folder Organizer")
            break;

        if not os.path.exists(user):
             print("Path not found. Please try again")

        else:
             organize_folder(user)
             print("Organisation complete!")
             break

       
 
             
if __name__ == "__main__":
     main()             
          





            

    

