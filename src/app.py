import request
from bs4 import BeautifulSoup

page = request.get_web_page('https://www.ptt.cc/bbs/Beauty/index.html')

def get_articles(dom, date):
  articles = []
  soup = BeautifulSoup(dom, 'html.parser')
  for div in soup.find_all('div', 'r-ent'):
    if div.find('div', 'date').string == date:
      article = {
        'push': 0,
        'author': '',
        'href': '',
        'title': ''
      }
      if div.find('div', 'nrec').string:
        try:
          article['push'] = int(div.find('div', 'nrec').string)
        except:
          print(div.find('div', 'nrec').string)
          print('err')
          pass
      if div.find('div', 'author').string:
        article['author'] = div.find('div', 'author').string

      if div.find('a'):
        article['href'] = div.find('a')['href']
        article['title'] = div.find('a').string
        articles.append(article)
  return articles    



articles = get_articles(page, '10/08')
for article in articles:
  print(article)
  print(end='\n')
