import requests
user_id = 5756720

url = 'https://www.kinopoisk.ru/user/2092256/votes/'


r = requests.get(url)

f = open('url.txt', 'w')
f.write(r.text)
f.close
