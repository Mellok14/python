#1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import json
from pprint import pprint
main_link = 'https://api.github.com'
header = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
name='Mellok14'
data = None
repos = requests.get(f'{main_link}/users/{name}/repos')
data = repos.json()
print(f'Список репозиториев пользователя {name}:')
for repositories in data:
    print(repositories['html_url'])

#Если я правильно понял что в json файл надо сохранить весь вывод то:

with open("1_result.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

