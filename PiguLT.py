"""4. Užduotis:
    [+] Išskirkite informaciją apie produktų kainas ir jų kategorijas iš pigu.lt puslapio naudodami Beautiful Soup 
    ir išsaugokite juos į Pandas DataFrame.
    [+]  Remdamiesi gautais duomenimis sukurkite stulpelinę diagramą, 
    kurioje bus pavaizduotos produktų kainos pagal kategorijas mažėjančia tvarka."""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time
import re
import numpy as np

delay = 2

url = "https://pigu.lt/lt/"

response = requests.get(url)

#tikriname ar uzklausa buvo sekminga (kad neulauzti svetaines)
if response.status_code == 200:
    # print("Status code:" + str(response.status_code))

    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    categorie_links = soup.find_all('a', class_='departament-link')
    

    categories = []
    prices = []
    products = []

    counter = 0  #kadangi imam daug duomenu, ir kad nelauzyti svetaines, kai programa ras 1000 produktu, programa sustos (kad nesuktu visu 3mln)

    for link in categorie_links[:10]:

        category_url = f"{link['href']}" 
        category_name = link.text.strip()
        
        category_response = requests.get(category_url)

        category_content = category_response.content
        category_soup = BeautifulSoup(category_content, 'html.parser')

        product_price = category_soup.find_all('div', class_='product-price') #div kodo blokas kuriame yra daug elementu
        product_name = category_soup.find_all('p', class_='product-name') #p yra paragraph
        #reikia dar 1 for kad eitu per produktu kainas ir jas pridetu i musu lista su kategorijomis
        for price, name in zip(product_price, product_name):
            # pasaliname nereikalinga teksta salia kainos naudojant regex
            numeric_price = re.sub('[^0-9]', '', price.text.strip())
            prices.append(numeric_price)
            categories.append(category_name)
            products.append(name.text.strip())
            counter += 1

            if counter == 1000:
                break
        if counter == 10:
            break

df = pd.DataFrame({
    'kategorija': categories,
    'kaina': prices,
    'produktas': products
})

#replace empty strings with a default value
df['kaina'].replace('', 0, inplace=True)

#replace non-finite values (NA or inf) with a default value
df['kaina'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)

# Convert the kaina column to float with two decimals after comma
df['kaina'] = df['kaina'].astype(float).round(2)
pd.options.display.float_format = '{:.2f}'.format

# Calculate average price for each category
avg_price_by_location = df.groupby('kategorija')['kaina'].mean().sort_values(ascending=False)
print(avg_price_by_location)