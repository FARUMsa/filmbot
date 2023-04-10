from bs4 import BeautifulSoup
import requests

async def get_FilmsMe(name, web):
    url=f'https://www.kinopoisk.ru/index.php?kp_query={name}'
    request=requests.get(url)
    for i in request.history:
        rst=i.url
        if rst[0:30]=='https://www.kinopoisk.ru/film/':
            return web+rst[24:-1]

    soup=BeautifulSoup(request.text, "html.parser")
    a=soup.find('p', class_='name')
    rt=a.find('a')['href'][:-6]
    if a.find('a').text[-7:-1] == 'сериал':
        rt=rt.replace('film', 'series')
    return web+rt

