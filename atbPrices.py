from checkAtbSearch import check_atb_search
from infoAboutProductsInPage import info_about_products_in_page
from checkAtbCatalog import check_atb_catalog

#поиск по страницам
product = 'сыр'

product_page = ''
catalog_result = check_atb_catalog(product)
search_result = check_atb_search(product)

if catalog_result:
    product_page = catalog_result
    print('Product is in the catalog')
elif search_result:
    product_page = search_result
    print('Product isn\'t in the catalog')
else:
    print('The product not found(')


info_about_products_in_page(product_page)




