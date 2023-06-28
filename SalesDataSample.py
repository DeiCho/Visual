import pandas as pd
import matplotlib.pyplot as plt

# sales_data_sample.csv
df = pd.read_csv('sales_data_sample.csv', encoding="ISO-8859-1")
# 1.Suskirstykite klientus pagal šalį.
# group_clients_by_country = df.groupby('COUNTRY')

# plt.figure(figsize=(12, 8))
# group_clients_by_country.size().plot(kind='bar') 

# plt.title('Klientai pagal salis')
# plt.xlabel('Salys')
# plt.ylabel('Klientai')
# plt.show()

# 2.Atrinkite užsakymus, kurių suma viršija 1000 eurų
# df['TOTAL'] = df['QUANTITYORDERED'] * df['PRICEEACH']

# group_by_order = df[df['TOTAL'] > 5000][['CUSTOMERNAME', 'TOTAL']]

# df.to_csv('sales_data_sample.csv', index=False)

# print(group_by_order)

# 3.Išfiltruokite užsakymus, kurie buvo pristatyti nuo 2003/9/30 iki 2005/03/15 .
# df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], format='%d/%m/%Y %H:%M', errors='coerce') 
# filtered_data = df[(df['ORDERDATE'] >= '9/30/2003') & (df['ORDERDATE'] <= '3/15/2005')]
# print(filtered_data)

# 4.Išfiltruokite užsakymus, kurių statusas 'Disputed';
# filtered_data = df[df['STATUS'] == 'Disputed']
# print(filtered_data)



# 5.Sukurkite skritulinę diagramą, kurioje būtų pavaizduota klientų skaičiaus pasiskirstymas pagal šalis

# plt.figure(figsize=(12, 8))
# group_clients_by_country_bar = df['COUNTRY'].value_counts().nlargest(10) #nlargest atrenka top10

# plt.bar(group_clients_by_country_bar.index, group_clients_by_country_bar.values)
# plt.title('Klientai pagal salis')
# plt.xlabel('Salys')
# plt.xticks(rotation=90) #pasuka texta x asyje
# plt.ylabel('Klientai')
# plt.show()
