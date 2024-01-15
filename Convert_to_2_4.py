import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3

def remove_replaygain_mutagen(file_path):
    mp3 = MP3(file_path)
    if 'RGAD' in mp3:
        del mp3['RGAD']
    mp3.save()

def convert_to_id3v2_4_mutagen(file_path):
    audio = MP3(file_path, ID3=ID3)

    # Set ID3v2.4 version
    audio.tags.version = (2, 4, 0)

    # Save changes
    audio.save()

if __name__ == "__main__":
    folder_path = "E:/Test_folder"  # Replace with the actual path to your folder
    
    # Remove ReplayGain frames and convert to ID3v2.4 for files in Test_folder
    for file in os.listdir(folder_path):
        if file.endswith(".mp3"):
            file_path = os.path.join(folder_path, file)
            print(f"Removing ReplayGain from {file_path}")
            remove_replaygain_mutagen(file_path)

            print(f"Converting {file_path} to ID3v2.4")
            convert_to_id3v2_4_mutagen(file_path)