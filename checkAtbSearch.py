import requests

import fake_useragent

user = fake_useragent.UserAgent().random
header = { 'User-Agent': user}

def check_atb_search(product):
    link_search_product = f'https://www.atbmarket.com/sch?page=1&lang=uk&location=1154&query={product}' 
    products_page = requests.get(link_search_product, headers = header).text

    return products_page