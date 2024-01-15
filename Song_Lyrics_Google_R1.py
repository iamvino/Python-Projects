from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Note: Chrome options work for Edge as well
from bs4 import BeautifulSoup
import os
import eyed3
import langid

     
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

        soup = BeautifulSoup(page_source, 'lxml')
        search_results = soup.find('div', {'jsname': 'WbKHeb'})

        lyrics_content = search_results.get_text("\n")
        print(f"{lyrics_content}")

        return lyrics_content
    except Exception as e:
        print(f"Error processing file {query}: {e}")

# Get all files in the folder with a specific extension (e.g., .mp3)
def process_files(folder_path):
    for filename in os.listdir(folder_path):
        # Check if file is an MP# file
        if filename.lower().endswith('.mp3'):
            file_path = os.path.join(folder_path, filename)
            audiofile = eyed3.load(file_path)

            # Check if USLT frame is None
            if audiofile is not None and audiofile.tag is not None:
                if not audiofile.tag.lyrics:
                    song_title = audiofile.tag.title
            
                    # Perform a Google search and get the home page content
                    lyrics_content = get_google_search_results(song_title)

                    # Check if lyrics_content is not None before classifying its language 
                    if lyrics_content is not None:
                        # Identify the language of the text
                        lang, _ = langid.classify(lyrics_content)

                        # Check the identified language is Tamil
                        if lang == 'ta':
                            # Save the lyrics to a text file
                            audiofile.tag.lyrics.set(lyrics_content)
                            audiofile.tag.save(version=(2,4,0))
                            print(f"Lyrics for '{song_title}' saved to: {file_path}")
                        else:
                            print(f"Lyrics not saved for '{song_title}' due to non-Tamil content.")
                    else:
                        print(f"Lyrics section not found for '{song_title}'.")
                else:
                    print(f"Lyrics found for file: {file_path}")

if __name__ == "__main__":
    folder_path = r"E:\Lyrics"
    process_files(folder_path)

