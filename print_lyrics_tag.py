import eyed3
import os

def print_lyrics_tag(folder_path, tags_to_print):
    # Traverse directory recursively
    for filename in os.listdir(folder_path):
        # Check if file is an MP3 file
        if filename.lower().endswith('.mp3'):
            file_path = os.path.join(folder_path, filename)
            audiofile = eyed3.load(file_path)

            # Check if USLT frame is None
            if audiofile is not None and audiofile.tag is not None:
                for tag_key in tags_to_print:
                    if tag_key in audiofile.tag.frame_set:
                            tag_value = audiofile.tag.frame_set[tag_key][0].text
                            print(f"Tag value for {file_path} - '{tag_key}': {tag_value}")

if __name__ == "__main__":
     folder_path = r"E:\Test"
     tags_to_print = [b'USLT', b'SYLT', b'TYER', b'TDRC']

     print_lyrics_tag(folder_path, tags_to_print)
     
