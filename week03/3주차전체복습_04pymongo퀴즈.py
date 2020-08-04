# 이 세줄은 항상 기본값
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie=db.movies.find_one({'title': '월-E'})
target_star=target_movie['score']


same_score=list(db.movies.find({'score':target_star}))
for i in same_score:
    print(i['title'])
    db.movies.update_many({'age': 40}, {'$set': {'age': 70}})


db.movies.update_many({'score': target_star}, { '$set': {'score': 0}})


