import eyed3
import csv
import os

# Specify the directory you want to start from
folder_path = r'E:\Test'

# Open the CSV file in write mode
with open("E:/Test/files_with_missing_lyrics.csv", 'w', newline='') as file:
    writer = csv.writer(file)

    # Traverse directory recursively
    for filename in os.listdir(folder_path):
        # Check if file is an MP3 file
        if filename.lower().endswith('.mp3'):
                file_path = os.path.join(folder_path, filename)
                audiofile = eyed3.load(file_path)

                # Check if USLT frame is None
                if audiofile is not None and audiofile.tag is not None:
                    if not audiofile.tag.lyrics:
                        # Write file path to CSV
                        writer.writerow([file_path])

