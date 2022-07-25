
# Importar Librerias para uso del Web Scraping
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Url a la cual quiero ingresar
url = 'https://simple.ripley.cl/tecno/celulares?source=menu&s=mdco'
# Descargar contenido la pagina con el URL
page = requests.get(url)
# Transformar a formato BeatifulSoup 
# Para identificar los elementos con HTML y acceder a lo que yo quiera
soup = BeautifulSoup(page.content, 'html.parser')

# Nombre Celulares
cel = soup.find_all('div', class_ ='catalog-product-details__name')

# Meter los celulares en una lista
celulares = list()

for i in cel:
        celulares.append(i.text)
print(celulares)

# Precios Celulares
pre = soup.find_all('li', class_='catalog-prices__offer-price')

precios = list()

for i in pre:
    precios.append(i.text)
print(precios)

# Dataframe
df = pd.DataFrame({'Celulares': celulares, 'Precios': precios})

# Guardar como csv
df.to_csv('Celulares y precios')