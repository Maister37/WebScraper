import requests
import json
from bs4 import BeautifulSoup


url = input("Input the URL: ")
try:
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(r.content, 'html.parser')

    try:
        if r.status_code != 200:
            print("Invalid movie page!")
        else:
            title = soup.find('h1').get_text()
            title = title.replace(u'\xa0', u' ').strip()
            description = soup.find('div', class_='summary_text').get_text()
            description = description.strip()
            movie_dict = {'title': title, 'description': description}
            print(movie_dict)
    except KeyError:
        print("Invalid movie page!")
except Exception:
    print('Invalid movie page!')