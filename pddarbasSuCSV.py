import pandas as pd
import matplotlib.pyplot as plt

# employees.csv
df = pd.read_csv('employees.csv')
# print(df)
#  * Apskaičiuoti vidurkį, sumą, minimumą, maksimumą ir kitus statistinius rodiklius stulpeliuose arba grupėse naudojant mean(), sum(), min(), max() ir kitas funkcijas.

# group_sizes = df.groupby('FIRST_NAME').size() 
# print(group_sizes)

# group_average = df.groupby('FIRST_NAME')['SALARY'].mean() 
# print(group_average)

# group_stats = df.groupby('FIRST_NAME')['SALARY'].describe() 
# print(group_stats)

# group_max = df.groupby('FIRST_NAME')['SALARY'].max() 
# print(group_max)

# * Grupuoti duomenis pagal tam tikrą stulpelį ir atlikti agregavimo operacijas, pvz., apskaičiuoti bendrą sumą ar vidurkį kiekvienai grupės naudojant groupby() funkciją.
# group_agg = df.groupby('FIRST_NAME').agg({'SALARY': ['sum', 'mean', 'max', 'size']}) 
# print(group_agg)



# * Atlikti reikiamus duomenų valymo veiksmus, pvz., pašalinti dublikatus, užpildyti trūkstamas reikšmes arba pašalinti netinkamas reikšmes.
# pasalinti_dublikatai = df.drop_duplicates(['FIRST_NAME'])
# print(pasalinti_dublikatai)


# * Sukurti naujus stulpelius, atlikdami skaičiavimus ar manipuliacijas su esamais stulpeliais, pvz., pridėti, sudėti arba suskaidyti reikšmes.

# df['increased_salary_10%'] = df.['SALARY'] * 1.1
# print(df)

# * Redaguoti duomenų tipus, pvz., konvertuoti skaičių tipo stulpelius į datų tipo stulpelius arba atvirkščiai.
# print(df.head())


# * Atlikti duomenų filtravimą, rūšiavimą ir sujungimą pagal sąlygas arba stulpelius.



# * Vizualizuoti duomenis naudojant įvairias diagramas ir grafikus
# group_agg = df.groupby('FIRST_NAME')['SALARY'].max()

# plt.title('Suvestines statiska pagal vardus ir ju atlyginimus')
# plt.xlabel('Vardas')
# plt.ylabel('Atlyginimas')
# group_agg.plot(kind='bar', figsize=(16, 4)) 
# plt.show()
