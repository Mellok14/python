import requests
import json
from pprint import pprint
main_link = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
appid='849A5BF12F9F10361EC8A0F599B59AB7'
steamids='76561198018314886'

response = requests.get(f'{main_link}?key={appid}&steamids={steamids}',headers=header)

pprint(response.json())
data = response.json()

with open("2_result.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

#А вот Яндекс почему то выдавал постоянно ошибку:
#{"statusCode":403,"error":"Forbidden","message":"Invalid key"}

main_link = 'https://search-maps.yandex.ru/v1/'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
appid='1ee6d950-9aac-4e20-b677-4e12a227dbef'
params={
    'text':'Wildberries',
    'lang': 'ru_RU',
    'apikey': appid
}
response = requests.get(main_link,headers=header,params=params)
pprint(response.json())

