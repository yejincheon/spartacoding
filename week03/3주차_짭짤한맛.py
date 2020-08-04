#mongoDB
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.
#crawling
import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs=soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for i in trs:
    rank=i.select_one('td.number').text[0:2].strip()
    name=i.select_one('td.info > a.title.ellipsis').text.strip()
    singer=i.select_one('td.info > a.artist.ellipsis').text.strip()

    print(rank,name,singer)
    db.ginie.insert_one({'순위':rank ,'곡명':name, '가수명':singer})



