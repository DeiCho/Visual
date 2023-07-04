import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time
from psydb_config import create_table, insert_query, db_params, take_database_info



delay = 2

for i in range(1, 5):
    url = f"https://en.aruodas.lt/gyvenamieji-namai/puslapis/{i}/?FBuildingType=box"
    
    time.sleep(delay)

    response = requests.get(url)

    content = response.text

    soup = BeautifulSoup(content, 'html.parser')

    skelbimai = soup.find_all('div', class_='list-row-v2 object-row selhouse advert')
    duomenys = []
    unikalus_duomenys = set() #naudojamas unikalioms reiksmems

    for skelbimas in skelbimai:
        kaina = skelbimas.find('span', class_='list-item-price-v2').text.strip()
        lokacija = skelbimas.select_one('.list-adress-v2 h3').text.strip() #h3 teksto dydis
        plotas = skelbimas.find('div', class_='list-AreaOverall-v2 list-detail-v2').text.strip()
        kaina = ''.join(c for c in kaina if c.isdigit())

        unikalus_ID = (kaina, lokacija, plotas)
        if (unikalus_ID) not in unikalus_duomenys:
            unikalus_duomenys.add(unikalus_ID)
            if ',' in lokacija:
                lokacija = lokacija.split(',')[0].strip() #po kablelio paima pirma reiksme - miesta (cia 0 - pirma reiksme)
            duomenys.append((kaina, lokacija, plotas))
            
            
    # df = pd.DataFrame(duomenys)
    # print(df)


    # df['kaina'] = pd.to_numeric(df['kaina'])
    # avg_price_by_location = df.groupby('lokacija')['kaina'].mean()
    # print(avg_price_by_location) #sugrupavom puslapio kainu vidurkius pagal lokacija (bet nera pilnai teisingi duomenys)


    # create_table()
    # insert_query(duomenys)

# data_from_aruodas_db = take_database_info()
# df = pd.DataFrame(data_from_aruodas_db, columns=['kaina', 'lokacija', 'plotas'])
# print(df)