import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time

delay = 2

for i in range(1, 5):
    url = "https://en.aruodas.lt/gyvenamieji-namai/"
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

            duomenys.append({
                'kaina': kaina,
                'lokacija': lokacija,
                'plotas': plotas
            })

    df = pd.DataFrame(duomenys)
    print(df)
