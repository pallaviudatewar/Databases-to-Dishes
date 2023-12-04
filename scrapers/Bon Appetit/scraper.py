import requests 
from bs4 import BeautifulSoup 
import json 

headers = {
    'accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
    'Accept-Language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
    'referer': 'https://www.google.com/',
}

def scrape_page(url):
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.text , features = 'lxml')

    main = json.loads(soup.find_all('script' , attrs={'type':'application/ld+json'})[0].contents[0])
    return main
