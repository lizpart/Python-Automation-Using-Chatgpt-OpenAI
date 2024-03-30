import requests
from bs4 import BeautifulSoup
import googletrans

# Get the page
url = 'https://www.techworld-with-nana.com/post/a-guide-of-how-to-get-started-in-it-in-2023-top-it-career-paths'
page = requests.get(url)

# Parse the page
soup = BeautifulSoup(page.content, 'html.parser')

# Get all the header elements
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Translate each header to Spanish
translator = googletrans.Translator()
spanish_headers = []
for header in headers:
    translated_header = {
        "text": translator.translate(header.text, dest='es').text,
        "name": header.name
    }

    spanish_headers.append(translated_header)

# Create an HTML file with the Spanish headers
with open('spanish_headers.html', 'w') as f:
    f.write('<html>\n')
    for header in spanish_headers:
        f.write(f'<{header["name"]}>{header["text"]}</{header["name"]}>\n')
    f.write('</html>\n')