import requests
from bs4 import BeautifulSoup
import string


url = 'https://www.nature.com/nature/articles'
try:
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(r.content, 'html.parser')

    try:
        if r.status_code != 200:
            print(f"The URL returned {r.status_code}")
        else:
            tags = list(enumerate(tag.get_text() for tag in soup.find_all('span', class_="c-meta__type")))
            print(tags)
            links = list(enumerate(
                link['href'] for link in soup.find_all('a', class_="c-card__link u-link-inherit", href=True)))
            print(links)
            for i in range(len(tags)):
                if 'News' == tags[i][1]:
                    article_link = requests.get(
                     'https://www.nature.com' + links[i][1], headers={'Accept-Language': 'en-US,en;q=0.5'})
                    article_soup = BeautifulSoup(article_link.content, 'html.parser')
                    article_title = article_soup.find('h1').get_text()
                    article_title = article_title.translate(str.maketrans('', '', string.punctuation))
                    article_title = article_title.replace(' ', '_')
                    article = article_soup.find("div", class_='article__body cleared').text.strip()
                    article_file = open('%s.txt' % article_title, 'w', encoding='UTF-8')
                    article_file.write(article)
                    article_file.close()
    except KeyError:
        print(f"The URL returned {r.status_code}")
except Exception:
    print(f"The URL returned {r.status_code}")