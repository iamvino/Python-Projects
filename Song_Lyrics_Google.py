from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Note: Chrome options work for Edge as well
from bs4 import BeautifulSoup
import os
import eyed3
import langid

# Function to get the title tag from an MP3 file
def get_mp3_title(mp3_file_path):
    audiofile = eyed3.load(mp3_file_path)
    if audiofile.tag.title:
        return audiofile.tag.title
    else:
        print(f"Title tag not found for '{mp3_file_path}'. Using the file name.")
        return os.path.splitext(os.path.basename(mp3_file_path))[0]

# Function to perform a Google search and get the home page content
def get_google_search_results(query):
    try:
        # Create a new Edge WebDriver instance
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument('--headless')
        driver = webdriver.Edge(options=edge_options)

        # Perform a Google search
        search_url = f"https://www.google.ca/search?q={query.replace(' ', '+')}+lyrics"
        driver.get(search_url)

        # Wait for the page to load (you may need to adjust the wait time)
        driver.implicitly_wait(1)

        # Get the HTML content of the page
        page_source = driver.page_source

        # Close the WebDriver
        driver.quit()

        return page_source
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to extract lyrics from the search results content
def extract_lyrics_from_search_results(content):
    soup = BeautifulSoup(content, 'lxml')  # Use 'lxml' as the parser
    
    lyrics_div = soup.find('div', {'jsname': 'WbKHeb'})

    if lyrics_div:
        return lyrics_div.get_text("\n")
    else:
        return None

# Folder containing MP3 files
folder_path = "E:/Music"

save_path = "E:/Lyrics"

# Get all files in the folder with a specific extension (e.g., .mp3)
mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]

for mp3_file in mp3_files:
    mp3_file_path = os.path.join(folder_path, mp3_file)
    
    # Extract song title from the title tag or use the file name
    song_title = get_mp3_title(mp3_file_path)

    # Perform a Google search and get the home page content
    search_results = get_google_search_results(song_title)

    if search_results:
        # Extract lyrics from the search results
        lyrics_content = extract_lyrics_from_search_results(search_results)

        # Check if lyrics_content is not None before classifying its language 
        if lyrics_content is not None:
            # Identify the language of the text
            lang, _ = langid.classify(lyrics_content)

            # Check the identified language is Tamil
            if lang == 'ta':
                # Save the lyrics to a text file
                file_path = os.path.join(save_path, f"{song_title.replace(' ', '_')}_Lyrics.txt")
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(lyrics_content)
                print(f"Lyrics for '{song_title}' saved to: {file_path}")
            else:
                print(f"Lyrics not saved for '{song_title}' due to non-Tamil content.")
        else:
            print(f"Lyrics section not found for '{song_title}'.")
    else:
        print(f"Search results not available for '{song_title}'.")
