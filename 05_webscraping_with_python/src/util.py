# A set of functions usefull for the purpose of scraping a website

import requests
from lxml.html import fromstring
import numpy as np
def get_proxies(entries=1):
    '''
    Function to get a list of some active proxies from https://free-proxy-list.net/. This code could change when the website updates its structure.
    Source: https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/
    '''
        
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    max_entries = len(parser.xpath('//tbody/tr'))
    
    url = 'https://httpbin.org/ip'
    
    while len(proxies) < entries:
        pick = np.random.randint(0, max_entries)
        ii = parser.xpath('//tbody/tr')[pick]
        print(f'Grapped {len(proxies)} proxies so far...')
        if ii.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([ii.xpath('.//td[1]/text()')[0], ii.xpath('.//td[2]/text()')[0]])
                
            try:
                response = requests.get(url,proxies={"http": proxy, "https": proxy})
                print(response.json())
                proxies.add(proxy)
            except:
                #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
                #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
                print("Skipping. Connnection error. Hang on.")

        
            
    print(f'\nDone!\nGrapped {len(proxies)} proxies.')
    return proxies

def get_user_agents():
    """
    Function to return a random user agent
    """
    url = 'https://udger.com/resources/ua-list/browser-detail?browser=Firefox'
    response = requests.get(url)
    parser = fromstring(response.text)
    user_agents = [x for x in parser.xpath("//div[@id='container']/table//tr[11]//text()") if x.startswith('Mozilla')]
    return np.random.choice(user_agents)