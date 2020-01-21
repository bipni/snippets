from pymongo import MongoClient

db_model = {
    "_id": "",
    "camera": "",
    "first_seen": "",
    "last_seen": 10
}

model_keys = []

client = MongoClient('localhost:27017')
db = client.test

data = db.temp.find()

for d in data:
    db_keys = list(d.keys())
    print(db_keys)
    break

for x in db_model:
    model_keys.append(x)

print(model_keys)

for field in db_keys:
    if field not in model_keys:
        data = db.temp.find()
        for d in data:
            db.temp.update_one(
                {'_id': d['_id']},
                {'$unset': {field: ""}}
            )


for field in model_keys:
    if field not in db_keys:
        data = db.temp.find()
        for d in data:
            db.temp.update_one(
                {'_id': d['_id']},
                {'$set': {field: db_model[field]}}
            )        


