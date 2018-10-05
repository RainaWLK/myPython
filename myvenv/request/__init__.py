import requests

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


