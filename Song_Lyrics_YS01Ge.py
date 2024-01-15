from selenium import webdriver
from bs4 import BeautifulSoup

song_title = "Rathamaarey"
URL = f"https://www.google.com/search?q={song_title}+Lyrics"

# Specify the path to the EdgeDriver executable (download it from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
edge_driver_path = r"C:\Users\evino\Downloads\edgedriver_win64\msedgedriver.exe"

# Set up the Edge browser
options = webdriver.EdgeOptions()
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # Example path, adjust as needed
# Add any additional options as needed

# Create a new instance of the Edge driver
driver = webdriver.Edge(options=options)

# Open the URL in the Edge browser
driver.get(URL)

# Wait for the page to load (you may need to adjust the wait time)
driver.implicitly_wait(10)

# Get the page source after waiting
page_source = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find the correct tag and class based on the structure of the Google search results page
song_contents = soup.find('div', {'jsname': 'WbKHeb'})  # Replace 'YOUR_CORRECT_CLASS_HERE' with the actual class

if song_contents:
    # Print the contents to the console
    print(song_contents.get_text())

    # Save the contents to a .txt file
    with open("song_lyrics.txt", "w", encoding="utf-8") as file:
        file.write(song_contents.get_text())
    print("Lyrics saved to '{song_title}'_Lyrics.txt")
else:
    print("Lyrics not found on the page.")