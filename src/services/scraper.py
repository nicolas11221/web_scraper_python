
# Importar Librerias para uso del Web Scraping
from bs4 import BeautifulSoup
import requests

# Url a la cual quiero ingresar
url = 'https://simple.ripley.cl/tecno/celulares?source=menu&s=mdco'


def get_html(url):
    # Obtener el html de la url
    html = requests.get(url)
    return html

def get_data(html, element, element_class):
    # Obtener el html de la url
    soup = BeautifulSoup(html.content, 'html.parser')
    # Obtener el html de la url
    data = soup.find_all(element, class_=element_class)
    return data


def data_handler(data):
    lista = []
    for i in data:
        lista.append(i.text)
    return lista

