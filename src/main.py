from services.scraper import get_html, get_data, data_handler

urls = [{
    "url": 'https://simple.ripley.cl/tecno/celulares?source=menu&s=mdco',
    "element1": 'div',
    "element_class1": 'catalog-product-details__name',
    "element2": 'li',
    "element_class2": 'catalog-prices__offer-price',
},{
    "url": "",
    "element1":"",
    "element_class1":"",
    "element2":"",
    "element_class2":"",
}]

def main(url):
    for url in urls:
        html = get_html(url['url'])
        cel = get_data(html, url['element1'], url['element_class1'])
        price = get_data(html, url['element2'], url['element_class2'])
        celulares = data_handler(cel)
        precios = data_handler(price)
        print(celulares, precios)

main(urls)
