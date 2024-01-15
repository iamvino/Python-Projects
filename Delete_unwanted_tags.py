import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3

def remove_unwanted_tags(file_path, wanted_tags):
    audio = MP3(file_path, ID3=ID3)

    # Remove unwanted tags
    for tag in list(audio.tags.keys()):
        if tag not in wanted_tags:
            del audio.tags[tag]

    # Set ID3v2.4 version
    audio.tags.version = (2, 4, 0)

    # Save changes
    audio.save()

if __name__ == "__main__":
    folder_path = "E:/Test_folder"  # Replace with the actual path to your folder
    wanted_tags = ['TALB', 'TPE1', 'TPE2', 'TCOM', 'TIT2', 'TRCK', 'TYER']
    
    # Convert to ID3v2.4 and remove unwanted tags for files in Test_folder
    for file in os.listdir(folder_path):
        if file.endswith(".mp3"):
            file_path = os.path.join(folder_path, file)
            print(f"Converting {file_path} to ID3v2.4 and removing unwanted tags")
            remove_unwanted_tags(file_path, wanted_tags)
