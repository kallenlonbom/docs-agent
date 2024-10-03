from bs4 import BeautifulSoup
import urllib
import requests
import os

# convert page address to numeric id
def to_id(input):
    input = input.split('#', 1)[0]
    input = input.encode('utf-8')
    id = int.from_bytes(input, 'little')
    return str(id)[-10:]

# recursive function to download given page and all linked subpages of original input page
def crawl(url, folder, origin=False):
    # make folder of given name
    if not os.path.exists(folder):
        os.makedirs(folder)
    print('Downloading ' + url)
    ext = '.txt'
    # set original input page
    if isinstance(origin, bool):
        origin = url
    # save page if html and no error
    request = requests.get(url)
    if request.ok and 'html' in request.headers['Content-Type']:
        html = request.text 
        soup = BeautifulSoup(html, "html.parser")
        id = to_id(url)
        with open(folder + "/" + str(id) + ext, 'w', encoding='utf-8') as file:
            file.write(url)
            file.write(soup.get_text())
            # crawl all linked subpages if not already downloaded
        for link in soup.find_all("a", href=True):
            link = urllib.parse.urljoin(url, str(link["href"]))
            if link.startswith(origin) and (to_id(link) + ext) not in os.listdir(folder):
                crawl(link, folder, origin)
    elif 'html' in request.headers['Content-Type']:
        print(f'Error downloading page {url} - {str(request.status_code)}')
    else:
        print('Skipped - not HTML file')