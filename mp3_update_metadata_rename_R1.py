import os
import eyed3
import logging
import langid
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def update_metadata(file_path, tag_search_terms, tags_to_update):
    # Use the updated file path from the rename_filename function
    audiofile = eyed3.load(file_path)

    # Check if the file exists before attempting to load
    if audiofile is None:
        print(f"Error: Could not load the file: {file_path}")

        for tag_key in tags_to_update:
            if tag_key in audiofile.tag.frame_set:
                tag_value = audiofile.tag.frame_set[tag_key][0].text

            for search_term in tag_search_terms:
                if search_term in tag_value:
                    # Delete portion from the search term to the end of the tag value
                    updated_tag_value = tag_value.split(search_term)[0].strip()
                    audiofile.tag.frame_set[tag_key][0] = eyed3.id3.frames.TextFrame(tag_key, updated_tag_value)

                    print(f"Updated {tag_key} tag value: {tag_value} -> {updated_tag_value}")
                    break # Stop searching if a match is found

        # Save changes to the file
        audiofile.tag.save(version=(2,4,0))

def delete_tags(file_path, unwanted_tags):
    audiofile = eyed3.load(file_path)

    if audiofile is None:
        print(f"Error: Could not load file {file_path}")
        return

    # Print existing tags and values
    print(f"Tags for {file_path}:")
    for tag in list(audiofile.tag.frame_set.keys()):
        tag_str = tag.decode('utf-8') if isinstance(tag, bytes) else tag
        if tag_str not in unwanted_tags and tag_str != b'IPLS':
            frame = audiofile.tag.frame_set[tag][0]

            # Check if it's a text frame or a URL frame
            if isinstance(frame, eyed3.id3.frames.TextFrame):
                tag_value = frame.text

                # Remove unwanted tags
                if tag_str in unwanted_tags:
                    del audiofile.tag.frame_set[tag]
                    
                    # Try decoding bytes
                    if isinstance(tag_value, bytes):
                        try:
                            tag_value = tag_value.decode('utf-8')
                        except UnicodeDecodeError:
                            tag_value = repr(tag_value)

                    print(f"Tag value of {tag_str} before: {tag_value}")

    # Save changes to the file
    audiofile.tag.save(version=(2,4,0))

def rename_filename(file_path, filename_search_terms):
    # Get the file name without extension
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))

    # Check if the search term is present in the file name
    for filename_search_term in filename_search_terms:
        # Heck if the search term is present in the file name
        if filename_search_term in file_name:
            # Rename the file by removing the portion from the search term to the end
            new_file_name = file_name.split(filename_search_term)[0].strip()
            new_file_name = f"{new_file_name}{file_extension}"

            # Construct the new file path
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

            try:
                # Rename the file
                os.rename(file_path, new_file_path)
                print(f"File renamed: {file_path} -> {new_file_path}")
                return new_file_path  # Return the updated file path
                
            except FileNotFoundError:
                print(f"Error: The file '{file_path}' was not found.")
            except Exception as e:
                print(f"Error: An unexpected error occurred while renaming the file: {e}")
        else:    
            logger.warning(f"Filename search term '{filename_search_term}' not found in '{file_path}'. File not renamed.")
    # Return the original file path if renaming fails or search term not found
    return file_path

def get_google_search_results(query, search_type):
    try:
        # Create a new Edge WebDriver instance
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument('--headless')
        driver = webdriver.Edge(options=edge_options)

        search_url = f"https://www.google.ca/search?q={query.replace(' ', '+')}"
        driver.get(search_url)

        # Wait for the page to load (you may need to adjust the wait time)
        driver.implicitly_wait(1)

        # Get the HTML content of the page
        page_source = driver.page_source

        # Close the WebDriver
        driver.quit()

        soup = BeautifulSoup(page_source, 'lxml')

        if search_type == 'USLT':
            search_results = soup.find('div', {'jsname': 'WbKHeb'})
        elif search_type == 'TYER':
            search_results = soup.find('div', {'class': 'Z0LcW t2b5Cf'})
        else:
            search_results = None

        return search_results.text if search_results else None
            
    except Exception as e:
        print(f"Error fetching Google search results for {query}: {e}")
        return None

def update_missing_tags(file_path, missing_tags):
    audiofile = eyed3.load(file_path)

    if audiofile is None:
        print(f"Error: Could not load {file_path}")
        return

    for missing_tag in missing_tags:
        missing_tag_str = missing_tag.decode('utf-8') if isinstance(missing_tag, bytes) else missing_tag
        missing_tag_value = None

        if missing_tag in audiofile.tag.frame_set:
            # Missing tag, generate query based on the tag
            if missing_tag == b'TYER':  # Release Year
                query = f"{audiofile.tag.album} release year"
                search_type = 'TYER'
            elif missing_tag == b'USLT':  # Lyrics
                query = f"{audiofile.tag.title} lyrics"
                search_type = 'USLT' 

            search_result = get_google_search_results(query, search_type)

            if search_result:
                if missing_tag == b'TYER':
                    try:
                        release_year = datetime.strptime(search_result, "%B %d, %Y").year
                        missing_tag_value = str(release_year)
                        audiofile.tag.frame_set[missing_tag][0] = eyed3.id3.frames.TextFrame(missing_tag, missing_tag_value)
                        print(f"Updated {missing_tag_str} tag value: {missing_tag_value}")
                    except ValueError:
                        print(f"Error parsing release year from {search_result}")

                elif missing_tag == b'USLT':
                    # You can update the lyrics here
                    if missing_tag_value is not None:
                        lang, _ = langid.classify(missing_tag_value)
                        if lang == 'ta':
                            audiofile.tag.save(version=(2,4,0))
                            print(f"Lyrics updated for '{missing_tag_str}' in: {file_path}.")
                        else:
                            print(f"Lyrics not updated for '{missing_tag_str}' due to non-Tamil content")
                    else:
                        print(f"Lyrics content not found for '{missing_tag_str}'.")

    # Save changes to the file
    audiofile.tag.save(version=(2,4,0))

def process_files(folder_path, unwanted_tags, tag_search_terms, tags_to_update, missing_tags):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            delete_tags(file_path, unwanted_tags)
            update_metadata(file_path, tag_search_terms, tags_to_update)
            update_missing_tags(file_path, missing_tags)

            audiofile = eyed3.load(file_path)
            track_title = audiofile.tag.title

            # Rename and delete after processing tags
            rename_filename(file_path, filename_search_terms)

if __name__ == "__main__":
    folder_path = "E:/Test"  # Replace with the path to your MP3 files or folder
    unwanted_tags = [b'TCON', b'WOAR', b'TCOP', b'TENC', b'TEXT', b'TIT1', b'TIT3', b'TOPE', b'TPE3', b'TPE4', b'TPUB', b'TSRC', b'WXXX', b'TIPL', b'USLT', b'COMM', b'TRSN', b'TSSE', b'TBPM', b'TLEN', b'WCOM', b'WOAF', b'WOAS', b'MCDI', b'WORS', b'TCMP', b'PRIV', b'RGAD']
    filename_search_terms = ['-Mass', '-Vmus', '...']
    tag_search_terms = [' - Mass', '...', '-Vmus', ' - Vmus', '-5Star', '-Star', '-SunM', '_NewT', ' - isai']
    tags_to_update = [b'TIT2', b'TPE1', b'TALB', b'TCOM', b'TPE2']
    missing_tags = [b'TYER', b'USLT']

    if os.path.isfile(folder_path):  # Check if the path is a file
        delete_tags(folder_path, unwanted_tags)
        update_metadata(folder_path, tag_search_terms, tags_to_update)
    elif os.path.isdir(folder_path):  # Check if the path is a directory
        process_files(folder_path, unwanted_tags, tag_search_terms, tags_to_update, missing_tags)
    else:
        print(f"Error: The path '{folder_path}' is not a valid file or directory.")
