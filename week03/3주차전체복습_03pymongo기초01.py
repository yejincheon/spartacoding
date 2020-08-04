# 이 세줄은 항상 기본값
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
import requests
from bs4 import BeautifulSoup#

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
trs=soup.select('#old_content > table > tbody > tr')

for i in trs:
    # old_content > table > tbody > tr:nth-child(2) > td.title > div > a
    title=i.select_one('td.title > div > a')


    if title is not None:
        rank = i.select_one('img')['alt']
        score = i.select_one('td.point')
        doc={'title':title.text,'rank':rank,'score':score.text}

        db.movies.insert_one(doc)

