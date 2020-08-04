import requests
from bs4 import BeautifulSoup

# 지금 내가 해야할거 : tr 돌면서 영화순위,영화제목,영화평점 가져오기

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#old_content > table > tbody > tr:nth-child(2)
trs=soup.select('#old_content > table > tbody > tr')

for i in trs:
    # old_content > table > tbody > tr:nth-child(2) > td.title > div > a
    title=i.select_one('td.title > div > a')
    rank=i.select_one('img')
    score=i.select_one('td.point')

    if title is not None:
        print(rank['alt'], title.text , score.text)



#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td.point
