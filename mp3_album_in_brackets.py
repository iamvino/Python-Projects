import os
import eyed3

def process_files(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".mp3"):
            file_path = os.path.join(folder_path, file_name)   
            file_name, file_extension = os.path.splitext(os.path.basename(file_path))

            new_file_name = file_name.split('_(')[0].strip()
            new_file_name = f"{new_file_name}{file_extension}"

            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

            os.rename(file_path, new_file_path)
            print(f"New file path: {new_file_path}")

            audiofile = eyed3.load(new_file_path)
            

            title = audiofile.tag.title

            album_start = title.find('(')
            print(f"Album start: {album_start}")
            album_end = title.find(')')
            print(f"Album end: {album_start}")
            if album_start != -1 and album_end != -1:
                album = title[album_start + 1:album_end]
                album_str = str(album)
                print(f"Album: {album}")
                audiofile.tag.album = album_str
            else:
                album = None
            
            new_title = title.split(' (')[0].strip()
            audiofile.tag.title = new_title

            audiofile.tag.save(version=(2,4,0))

if __name__ == "__main__":
    folder_path = "E:/Test"

    process_files(folder_path)