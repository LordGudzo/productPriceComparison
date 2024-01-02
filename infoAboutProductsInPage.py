from bs4 import BeautifulSoup

def info_about_products_in_page(page):
    soup = BeautifulSoup(page, "lxml")
    products_block = soup.find('div', class_ = "catalog-list")
    #search all products in the page
    catalog_item = products_block.find_all('article', class_ = 'catalog-item')

    for item in catalog_item:
        #search product name
        catalog_item_info = item.find('div', class_= "catalog-item__title").text
       
        def isPromotion():
            main_price = item.find('div', class_='catalog-item__product-price').find('data',\
                                                        class_='product-price__bottom')
            if main_price:
                return main_price['value']
            else:
                return False
            
    
        #search price promotion
        product_price = item.find('div', class_='catalog-item__product-price').find('data', class_='product-price__top')
        if isPromotion():
            print(f'{catalog_item_info} ---Promotion price: {product_price['value']} ---\
                main price: {isPromotion()}')
        else:
            print(f'{catalog_item_info} --- main price: {product_price['value']}')