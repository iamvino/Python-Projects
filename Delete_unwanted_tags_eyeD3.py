import os
import eyed3

def rename_filename(file_path, filename_search_term):
    # Get the file name without extension
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))

    # Check if the search term is present in the file name
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
            return new_file_path
            
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"Error: An unexpected error occurred while renaming the file: {e}")

    print(f"Search term '{filename_search_term}' not found in the file name: {file_path}")
    # Return the original file path if renaming fails or search term not found
    return file_path

def update_metadata(file_path, tag_search_term, tags_to_update):
    # Use the updated file path from the rename_filename function
    updated_file_path = rename_filename(file_path, filename_search_term)

    # Check if the file exists before attempting to load
    if os.path.exists(updated_file_path):
        print(f"Attempting to load file: {updated_file_path}")

        audiofile = eyed3.load(updated_file_path)

        if audiofile is None:
            print(f"Error: Could not load file {updated_file_path}")
            return

        # Update metadata in specified tags
        for tag_key in tags_to_update:
            if tag_key in audiofile.tag.frame_set:
                tag_value = audiofile.tag.frame_set[tag_key][0].text

                if tag_search_term in tag_value:
                    # Delete portion from the search term to the end of the tag value
                    updated_tag_value = tag_value.split(tag_search_term)[0].strip()
                    audiofile.tag.frame_set[tag_key][0] = eyed3.id3.frames.TextFrame(tag_key, updated_tag_value)

                    print(f"Updated {tag_key} tag value: {tag_value} -> {updated_tag_value}")

        # Save changes to the file
        audiofile.tag.save()
    else:
        print(f"Error: File not found - {updated_file_path}")

def delete_tags(file_path, unwanted_tags):
    # Use the updated file path from the rename_filename function
    updated_file_path = rename_filename(file_path, filename_search_term)

    # Check if the file exists before attempting to load
    if os.path.exists(updated_file_path):
        audiofile = eyed3.load(updated_file_path)

        if audiofile is None:
            print(f"Error: Could not load file {updated_file_path}")
            return

        # Print existing tags and values
        print(f"Tags for {updated_file_path}:")
        for tag in list(audiofile.tag.frame_set.keys()):
            tag_str = tag.decode('utf-8') if isinstance(tag, bytes) else tag
            if tag_str not in unwanted_tags and tag_str != b'IPLS':
                frame = audiofile.tag.frame_set[tag][0]

                # Check if it's a text frame or a URL frame
                if isinstance(frame, eyed3.id3.frames.TextFrame):
                    tag_value = frame.text
                elif isinstance(frame, eyed3.id3.frames.UrlFrame):
                    tag_value = frame.url
                elif isinstance(frame, eyed3.id3.frames.LyricsFrame):
                    tag_value = frame.text
                elif isinstance(frame, eyed3.id3.frames.CommentFrame):
                    # Handle CommentFrame
                    tag_value = f"Language: {frame.lang}, Description: {frame.description}, Text: {frame.text}"
                else:
                    # Handle other types of frames as needed
                    tag_value = str(frame)
                
                # Try decoding bytes
                if isinstance(tag_value, bytes):
                    try:
                        tag_value = tag_value.decode('utf-8')
                    except UnicodeDecodeError:
                        tag_value = repr(tag_value)

                print(f"Tag value of {tag_str} before: {tag_value}")

        # Remove unwanted tags
        for unwanted_tag in unwanted_tags:
            unwanted_tag_bytes = unwanted_tag.encode('utf-8') if isinstance(unwanted_tag, str) else unwanted_tag
            if unwanted_tag_bytes in audiofile.tag.frame_set:
                del audiofile.tag.frame_set[unwanted_tag_bytes]
                print(f"Removed tag: {unwanted_tag}")

        # Remove IPLS tag specifically
        if b'IPLS' in audiofile.tag.frame_set:
            del audiofile.tag.frame_set[b'IPLS']
            print("Removed IPLS frame")

        # Save changes to the file
        audiofile.tag.save()
    
        # Rename and delete after processing tags
        rename_filename(file_path, filename_search_term)
    else:
        print(f"Error: File not found - {updated_file_path}")

def process_files(folder_path, unwanted_tags):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            delete_tags(file_path, unwanted_tags)
            rename_filename(file_path, filename_search_term)
            update_metadata(file_path, tag_search_term, tags_to_update)

if __name__ == "__main__":
    folder_path = "E:/Test_folder"  # Replace with the path to your MP3 files or folder
    unwanted_tags = [b'TCON', b'WOAR', b'TCOP', b'TENC', b'TEXT', b'TIT1', b'TIT3', b'TOPE', b'TPE3', b'TPE4', b'TPUB', b'TSRC', b'WXXX', b'TIPL', b'USLT', b'COMM', b'TRSN', b'TSSE', b'TBPM', b'TLEN', b'WCOM', b'WOAF', b'WOAS', b'MCDI', b'WORS', b'TCMP', b'PRIV']
    filename_search_term = '-Mass'
    tag_search_term = ' - Mass'
    tags_to_update = [b'TIT2', b'TPE1', b'TALB', b'TCOM', b'TPE2']

    if os.path.isfile(folder_path):  # Check if the path is a file
        delete_tags(folder_path, unwanted_tags)
        rename_filename(folder_path, filename_search_term)
        update_metadata(folder_path, tag_search_term, tags_to_update)
    elif os.path.isdir(folder_path):  # Check if the path is a directory
        process_files(folder_path, unwanted_tags)
    else:
        print(f"Error: The path '{folder_path}' is not a valid file or directory.")
