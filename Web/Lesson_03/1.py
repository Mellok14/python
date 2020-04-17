import json
from pymongo import MongoClient
from pprint import pprint

#В одной функции выполним загрузку данных и сразу проверку на уникальность.
#Таким образом при поступлении обновленных данных от парсера в БД будут добавлены только новые записи.

def json_to_db(coll, file):
    with open(file, "r") as f:
        data = json.load(f)
    for doc in data:
        if coll.count_documents(doc) < 1:
            coll.insert_one(doc)
#Поиск по заданной зарплате
#В предыдущем ДЗ я не преобразовал зарплаты к int, пришлось вернуться и переделать там и потом сохранять в json
#Как я понимаю в Mongo преобразовать к int не так просто
def vacancies_price(coll, price: int):
    vacancies = coll.find({'min_price': {'$gt': price}})
    for i in vacancies:
        pprint(i)

file = 'Lesson02_result.json'
client = MongoClient('localhost', 27017)
db = client['vacancies']
coll = db.coll

json_to_db(coll, file)

vacancies_price(coll, 80000)

