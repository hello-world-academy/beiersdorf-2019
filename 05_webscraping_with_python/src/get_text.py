
from bs4 import BeautifulSoup
import requests

def get_text(urls):
    if not isinstance(urls, list):
        urls= [urls]
    full_texts = []
    for url in urls:
        page = requests.get(url)
        blog = BeautifulSoup(page.content, 'html.parser')
        print(f'Extracting {url}')
        text_segments = []
        for elem in blog.find_all('div', {"class" : 'rte'}):
            if elem.attrs['class'][0] == 'rte':
                text_segments.append(elem)
        full_text = ' '.join([s.get_text().replace('\r\n', ' ').strip() for s in text_segments])
        full_texts.append(full_text)
    print('\nDowload complete!')
    return full_texts
