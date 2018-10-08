from request import ptt
import datetime

page = ptt.get_web_page('https://www.ptt.cc/bbs/Beauty/index.html')

now = datetime.datetime.now()
articles = ptt.get_articles(page, now.strftime('%m/%d'))
for article in articles:
  print(article)
  print(end='\n')
