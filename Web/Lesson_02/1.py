import numpy as np
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
name = input('Введите название вакансии:')
next_page_link = 'https://hh.ru'
next_page = '/search/vacancy?clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=' + name
main_link = next_page_link + next_page
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
vacancies = []
while next_page != None:
    main_link = next_page_link + next_page
    html = requests.get(main_link, headers=header).text
    soup = bs(html, 'lxml')
    vakancy_block = soup.find_all('div', {'class': 'vacancy-serp'})[0]
    vakancy_list = vakancy_block.find_all('div', {'class': 'vacancy-serp-item'})
    for vakancy in vakancy_list:
        vakancy_data = {}
        vakancy_name = vakancy.find('a', {'class': 'bloko-link'}).getText()
        vakancy_price = vakancy.find('div', {'class': 'vacancy-serp-item__sidebar'}).getText()
        vakancy_link = vakancy.find('a', {'class': 'bloko-link'})['href']
        vakancy_site = 'hh.ru'
        vakancy_company = vakancy.find_all('a', {'class': 'bloko-link'})[1].getText()
        vakancy_location = vakancy.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).getText()
        vakancy_data['name'] = vakancy_name
        vakancy_data['price'] = vakancy_price
        vakancy_data['link'] = vakancy_link
        vakancy_data['site'] = vakancy_site
        vakancy_data['company'] = vakancy_company
        vakancy_data['location'] = vakancy_location
        vacancies.append(vakancy_data)
    if soup.find('a', {'data-qa': 'pager-next'}) == None:
        break
    else:
        next_page = soup.find('a', {'data-qa': 'pager-next'})['href']

def price(list):
    for i in list:
        if i['price'][0:2] == 'от':
            i['min_price'] = i['price'].split(' ')[1].replace('\xa0', '')
            i['max_price'] = None
            i['currency'] = i['price'].split(' ')[2]
        elif i['price'][0:2] == 'до':
            i['min_price'] = None
            i['max_price'] = i['price'].split(' ')[1].replace('\xa0', '')
            i['currency'] = i['price'].split(' ')[2]
        elif i['price'] == '':
            i['min_price'] = None
            i['max_price'] = None
            i['currency'] = None
        else:
            i['min_price'] = i['price'].split(' ')[0].split('-')[0].replace('\xa0', '')
            i['max_price'] = i['price'].split(' ')[0].split('-')[1].replace('\xa0', '')
            i['currency'] = i['price'].split(' ')[1]
        i.pop('price', None)

next_page_link_1 = 'https://russia.superjob.ru'
next_page_1 = '/vacancy/search/?keywords=' + name
main_link_1 = next_page_link_1 + next_page_1
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
vacancies_1 = []

while next_page_1 != None:
    main_link_1 = next_page_link_1 + next_page_1
    html = requests.get(main_link_1, headers=header).text
    soup = bs(html, 'lxml')
    vakancy_block = soup.find('div', {'class': 'f-test-vacancy-item'}).parent.parent
    vakancy_list = vakancy_block.findChildren('div', {'class': 'iJCa5'})
    for vakancy in vakancy_list:
        vakancy_data = {}
        vakancy_name = vakancy.find('div', {'class': '_3mfro'}).getText()
        vakancy_price = vakancy.find('span', {'class': '_3mfro'}).getText()
        vakancy_link = vakancy.find('a', {'target': '_blank'})['href']
        vakancy_site = 'https://superjob.ru'
        try:
            vakancy_company = vakancy.find('span', {'class': 'f-test-text-vacancy-item-company-name'}).getText()
        except AttributeError:
            vakancy_company = None
        vakancy_location = vakancy.find('span', {'class': 'f-test-text-company-item-location'}).next.next.next.next.next.getText()
        vakancy_data['name'] = vakancy_name
        vakancy_data['price'] = vakancy_price
        vakancy_data['link'] = vakancy_link
        vakancy_data['site'] = vakancy_site
        vakancy_data['company'] = vakancy_company
        vakancy_data['location'] = vakancy_location
        vacancies_1.append(vakancy_data)
    if soup.find('a', {'class': 'f-test-button-dalshe'}) == None:
        break
    else:
        next_page_1 = soup.find('a', {'class': 'f-test-button-dalshe'})['href']

def price_1(list):
    for i in list:
        if i['price'][0:2] == 'от':
            i['min_price'] = int(i['price'].split('\xa0')[1] + i['price'].split('\xa0')[2])
            i['max_price'] = None
            i['currency'] = i['price'].split('\xa0')[3]
        elif i['price'][0:2] == 'до':
            i['min_price'] = None
            i['max_price'] = int(i['price'].split('\xa0')[1] + i['price'].split('\xa0')[2])
            i['currency'] = i['price'].split('\xa0')[3]
        elif i['price'] == 'По договорённости':
            i['min_price'] = None
            i['max_price'] = None
            i['currency'] = None
        else:
            i['min_price'] = int(i['price'].split('—')[0].replace('\xa0', ''))
            i['max_price'] = int(i['price'].split('—')[1].split('\xa0')[1] + i['price'].split('—')[1].split('\xa0')[2])
            i['currency'] = i['price'].split('\xa0')[-1]
        i.pop('price', None)

price(vacancies)
price_1(vacancies_1)
df = pd.DataFrame(vacancies)
df_1 = pd.DataFrame(vacancies_1)
df_total = pd.concat([df, df_1], axis = 0)
for i in vacancies_1:
    vacancies.append(i)
with open("1_result.json", "w", encoding="utf-8") as file:
    json.dump(vacancies, file)