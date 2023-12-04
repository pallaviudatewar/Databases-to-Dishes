from bs4 import BeautifulSoup
import requests 
import json 

cookies = json.load(open('cookies.json' , 'rb'))

def scrape_recipe(url):
    page = requests.get(url , cookies=cookies)
    soup = BeautifulSoup(page.text , features="lxml")

    jsons = soup.find_all('script' , attrs = {'type':'application/ld+json'})
    return jsons[0].contents[0]

def scrape_blog(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text , features="lxml")

    data = soup.find_all('script' , attrs = {'type':'application/ld+json'})
    data = json.loads(data[0].contents[0])
    item_list = data['mainEntity']['itemListElement']
    recipes = [item['url'] for item in item_list]
    recipe_data = [json.loads(scrape_recipe(recipe)) for recipe in recipes]
    return recipe_data    

