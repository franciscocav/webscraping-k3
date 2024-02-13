# Bibliotecas que foram usadas para poder realizar este webscraping.

import pandas as pd
import requests
from bs4 import BeautifulSoup

website = "https://www.k3distribuidora.com.br/ecommerce/departamento/47/informatica/"
site = requests.get(website)
soup = BeautifulSoup(site, 'html.parser')
print(site.text)