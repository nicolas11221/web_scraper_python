from services.scraper import get_html, get_data, data_handler

url = [{
    "url": 'https://simple.ripley.cl/tecno/celulares?source=menu&s=mdco',
    "element1": 'div',
    "element_class1": 'catalog-product-details__name',
    "element2": 'li',
    "element_class2": 'catalog-prices__offer-price',
},]

def main(url):
    for i in url:
        html = get_html(i['url'])
        cel = get_data(html, i['element1'], i['element_class1'])
        price = get_data(html, i['element2'], i['element_class2'])
        celulares = data_handler(cel)
        precios = data_handler(price)
        print(celulares, precios)

main(url)
