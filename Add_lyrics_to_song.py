import os
import eyed3

def read_lyrics(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def add_lyrics_to_mp3(lyrics_folder, mp3_folder):
    for mp3_file in os.listdir(mp3_folder):
        if mp3_file.endswith('.mp3'):
            mp3_path = os.path.join(mp3_folder, mp3_file)

            audiofile = eyed3.load(mp3_path)
            if audiofile.tag and audiofile.tag.title:
                title = audiofile.tag.title.replace(" ", "_").lower()
                lyrics_file = os.path.join(lyrics_folder, f"{title}_lyrics.txt")

                if os.path.exists(lyrics_file):
                    lyrics = read_lyrics(lyrics_file)

                    audiofile.tag.lyrics.set(lyrics)
                    audiofile.tag.save()

                    print(f"Lyrics added to {mp3_file}")
                else:
                    print(f"Matching lyrics file not found for {mp3_file}")
            else:
                print(f"Title tag not found for {mp3_file}")

if __name__ == "__main__":
    lyrics_folder = "E:/Lyrics"
    mp3_folder = "E:/Test_folder"

    add_lyrics_to_mp3(lyrics_folder, mp3_folder)
