import requests
from bs4 import BeautifulSoup

def get_web_page(url):
  resp = requests.get(
    url = url,
    cookies={'over18': '1'}
  )
  if resp.status_code == 200:
    return resp.text
  else:
    print('Invalid url:'+url)
    return None

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

