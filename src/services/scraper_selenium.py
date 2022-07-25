
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By

# Url a la cual quiero ingresar
site_web = 'https://simple.ripley.cl/tecno/celulares?source=menu&s=mdco'
driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
driver.get(site_web)

# Metodo de como va a buscar los elementos
products = driver.find_elements_by_tag_name('div')

for product in products:
    print(product.text)

#page_change 
#<a href="?orderBy=sequence&amp;s=mdco&amp;source=menu&amp;page=3"><span aria-hidden="true">»</span></a>
#<a href="?orderBy=sequence&amp;s=mdco&amp;source=menu&amp;page=4"><span aria-hidden="true">»</span></a>

