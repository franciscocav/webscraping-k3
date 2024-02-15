# Bibliotecas que foram usadas para poder realizar este webscraping.

import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs
from datetime import date as dt

lista_produtos = []
lista_precos = []

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15"}

for i in range(1,13,1):
    website = f"https://www.k3distribuidora.com.br/ecommerce/departamento/47/informatica/{i}"
    site = rq.get(website, headers=headers)
    soup = bs(site.text, 'html.parser')
    produtos = soup.find_all('a', class_='Title')
    preco_parc = soup.find_all('span', class_='Preco Final')
    for produto in range(0, len(produtos)):
        lista_produtos.append(produtos[produto].text)
    for preco_parcelado in range(0, len(preco_parc)):
        lista_precos.append(preco_parc[preco_parcelado].text)

d = {"Produto": lista_produtos, "Preços": lista_precos}
df = pd.DataFrame(data=d)


df['Preços'] = df['Preços'].str.replace('R$ ', '')
df['Preços'] = df['Preços'].str.replace('.', '')
df['Preços'] = df['Preços'].str.replace(',', '.')
df['Produto'] = df['Produto'].str.upper()
df['Preços'] = df['Preços'].astype(float)
df['Preço a Vista'] = df['Preços']*0.95
df['Preço de Revenda'] = df['Preços']*1.1
df['Data de Atualização'] = dt.today()
df['Loja'] = 'K3 DISTRIBUIDORA'

with pd.ExcelWriter("extrato_k3_distribuidora.xlsx") as writer:
    df.to_excel(writer, sheet_name="Informática", index=False)
print("Webscraping Realizado com sucesso.")