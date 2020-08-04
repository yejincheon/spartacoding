from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

target = db.movies.find_one({'title': '월-E'})
target_star=target['score']
same_score=list(db.movies.find({'score':target_star}, {'_id': False}))

for i in same_score:
    print(i['title'])
    db.movies.update_many({'title': i['title']}, {'$set': {'score': 0}})


