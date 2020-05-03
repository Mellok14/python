from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['mvideo']


chrome_options = Options()
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.mvideo.ru/')

time.sleep(5)

next = driver.find_element_by_xpath('(//div[@class="gallery-content accessories-new "])[2]//a[(@class="next-btn sel-hits-button-next")]')
actions = ActionChains(driver)
while True:
    actions.move_to_element(next).click().perform()
    if 'disabled' in next.get_attribute('class'):
        break
items = driver.find_elements_by_xpath('(//div[@class="gallery-content accessories-new "])[2]//li[@class="gallery-list-item"]')
for item in items:
    item_data = json.loads(item.find_element_by_xpath('.//a[@data-product-info]').get_attribute('data-product-info'))
    db.hits.insert_one({'productId' : item_data['productId'],
                           'productVendorName' : item_data['productVendorName'],
                           'productName' : item_data['productName'],
                           'productPriceLocal' : item_data['productPriceLocal']})


