from bs4 import BeautifulSoup
import requests
import json

def save(object):
    json_response = json.dumps(object, indent=4, ensure_ascii=False,)
    with open('data_parsed.json', 'a', encoding='utf-8') as outfile:
        outfile.write(json_response)
        outfile.write('\n')

def parse():
    URL = 'https://habr.com/ru/all/'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('article', class_ = 'tm-articles-list__item')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('a', class_ = 'tm-article-snippet__title-link').get_text(strip = True),
            'author': item.find('a', class_ = 'tm-user-info__username').get_text(strip = True),
            'link': item.find('a', class_ = 'tm-article-snippet__title-link').get('href')
        })

        global comp
        for comp in comps:
            save(comp)

parse()
