from bs4 import BeautifulSoup
import requests



def get_blog_urls(base_url, blog_urls):
    '''
    Function to extract links from the Beiersdorf Blog website
    '''
    # make sure the argument is of type list 
    if not isinstance(blog_urls, list):
        blog_urls = [blog_urls]
    hyper_links = []
    # iterate over all urls
    for url in blog_urls:
        page = requests.get(base_url + url)
        soup = BeautifulSoup(page.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            hyper_link = article.find('a').get('href')
            hyper_links.append(base_url + hyper_link)
    print(f'{len(set(hyper_links))} links to articles were found!\n')
    return list(set(hyper_links))


def get_text(urls):
    if not isinstance(urls, list):
        urls= [urls]
    full_texts = []
    for url in urls:
        page = requests.get(url)
        blog = BeautifulSoup(page.content, 'html.parser')
        print(f'Exracting {url}')
        text_segments = []
        for elem in blog.find_all('div', {"class" : 'rte'}):
            if elem.attrs['class'][0] == 'rte':
                text_segments.append(elem)
        full_text = ' '.join([s.get_text().replace('\r\n', ' ').strip() for s in text_segments])
        full_texts.append(full_text)
    print('\nDowload complete!')
    return full_texts