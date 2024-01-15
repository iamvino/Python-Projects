import os
import requests
from bs4 import BeautifulSoup

# Function to search for Tamil song lyrics
def get_tamil_song_lyrics(song_name):
    # Replace this URL with the appropriate website
    url = f"https://www.tamilpaa.com/tamil-lyrics/?s={song_name.replace(' ', '+')}"

    # Fetch the search results page
    search_page = requests.get(url)
    soup = BeautifulSoup(search_page.content, 'html.parser')

    # Extract the URL of the first search result (assuming it contains the lyrics)
    lyrics_page_url = soup.find('a', href=lambda href: href and 'tamil-lyrics' in href)['href'] if soup.find('a', href=lambda href: href and 'tamil-lyrics' in href) else None

    if not lyrics_page_url:
        print(f"Lyrics not found for '{song_name}'.")
        return None

    # Fetch the lyrics page
    lyrics_page = requests.get(lyrics_page_url)
    soup = BeautifulSoup(lyrics_page.content, 'html.parser')

    # Extract the lyrics from the page (customize this based on the website structure)
    lyrics = soup.find(id='lyric').get_text() if soup.find(id='lyric') else None

    return lyrics

# Folder containing song files
folder_path = "C:/Path/To/Your/Folder"

# Get all files in the folder with a specific extension (e.g., .mp3)
song_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]

for song_file in song_files:
    # Extract song title from the file name (customize this based on your file naming convention)
    song_title = os.path.splitext(song_file)[0]

    # Search for lyrics
    lyrics = get_tamil_song_lyrics(song_title)

    if lyrics:
        # Save the lyrics to a text file
        lyrics_file_path = os.path.join(folder_path, f"{song_title}_Lyrics.txt")
        with open(lyrics_file_path, 'w', encoding='utf-8') as lyrics_file:
            lyrics_file.write(lyrics)

        print(f"Lyrics for '{song_title}' saved to: {lyrics_file_path}")
