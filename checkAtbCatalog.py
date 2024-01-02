import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = { 'User-Agent': user}
link_atb_main = 'https://www.atbmarket.com'

def check_atb_catalog(product):
    responce_main = requests.get(link_atb_main, headers=header).text
    soup = BeautifulSoup(responce_main, 'lxml')
    category_menu = soup.find('ul', class_='category-menu')
    category_menu_item = category_menu.find_all('li', class_='category-menu__item')
    for item in category_menu_item:
        products = item.find_all('li', class_="submenu__item")
        for i in products:
            if product.lower() in i.text.lower():
                link_product_page = f'{link_atb_main}{i.find('a').get('href')}'
                products_page = requests.get(link_product_page, headers=header).text

                return products_page
