from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Note: Chrome options work for Edge as well
from bs4 import BeautifulSoup
import os
import eyed3
import langid

def update_lyrics_tag(file_path, lyrics_content):
    audiofile = eyed3.load(file_path)

    print(f"Lyrics content for {file_path}:\n{lyrics_content}")

    # Set the lyrics tag for each line separately
    audiofile.tag.lyrics.set(lyrics_content)

    # Remove the TIPL frame
    tipl_frame_name = b'TIPL'  # Use byte representation
    if tipl_frame_name in audiofile.tag.frame_set:
        del audiofile.tag.frame_set[tipl_frame_name]
    
    # Remove the IPLS frame
    ipls_frame_name = b'IPLS'  # Use byte representation
    if ipls_frame_name in audiofile.tag.frame_set:
        del audiofile.tag.frame_set[ipls_frame_name]

    audiofile.tag.save(version=(2,4,0))

def process_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            audiofile = eyed3.load(file_path)

            updated_title = audiofile.tag.title

            if updated_title:
                search_results = get_google_search_results(updated_title)
                if search_results:
                    lyrics_content = extract_lyrics_from_search_results(search_results)
                    if lyrics_content is not None:
                        lang, _ = langid.classify(lyrics_content)
                        if lang == 'ta':
                            
                            update_lyrics_tag(file_path, lyrics_content)
                            print(f"Lyrics updated for '{updated_title}' in: {file_path}.")
                        else:
                            print(f"Lyrics not updated for '{updated_title}' due to non-Tamil content.")
                    else:
                        print(f"Lyrics section not found for '{updated_title}'.")
                else:
                    print(f"Search results not available for '{updated_title}'.")

def get_google_search_results(query):
    try:
        # Create a new Edge WebDriver instance
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument('--headless')
        driver = webdriver.Edge(options=edge_options)

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

def extract_lyrics_from_search_results(content):
    soup = BeautifulSoup(content, 'lxml')
    lyrics_div = soup.find('div', {'jsname': 'WbKHeb'})

    if lyrics_div:
        return lyrics_div.get_text("\n")
    else:
        return None

if __name__ == "__main__":
    folder_path = "E:/Test_folder"
    process_files(folder_path)
    print("File properties and lyrics updated successfully.")
