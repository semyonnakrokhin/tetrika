import requests
from bs4 import BeautifulSoup
import re

domain = 'https://ru.wikipedia.org'
url = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"

def get_subspecies(animals_list):
    return animals_list


def get_animals_dict(url, domain):
    current_letter = 'А'
    dict = {}.fromkeys('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ', [])
    while current_letter != 'A': #Это английская А, не русская
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')

        for data in soup.find('div', class_='mw-category mw-category-columns').find_all('div', class_='mw-category-group'):
            current_letter = data.find('h3').text
            if current_letter == 'A':
                break
            dict[current_letter] = dict[current_letter] + get_subspecies([ref.text for ref in data.find_all('a')])

        url = domain + soup.find('div', id='mw-pages').find('a', text=re.compile("Следующая страница")).get('href')
    return dict

dict = get_animals_dict(url, domain)
for letter in dict:
    print(f'{letter}: {len(dict[letter])}', end='\n')


