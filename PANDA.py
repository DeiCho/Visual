import pandas as pd
import matplotlib.pyplot as plt

"""         vienmate duomenu struktura(saugo vienos eilutes duomenis su indeksais)"""
# data = pd.Series([10, 20, 30, 40, 50])
# print(data)


"""         dvimate duomenu struktura(saugo duomenis lenteles pavidalu su stulpeliu ir eiluciu indeksais)"""
# data = {
#     'Name': ['Mantas', 'Deividas', 'Migle', 'Ausrine'],
#     'Age': [29, 27, 24, 45],
#     'City': ['Marijampole', 'Vilnius', 'Kaunas', 'Vilnius']
#     }

# df = pd.DataFrame(data) #df - dataframe, reiskia kad printinsim lentele
# print(df)

# print(df.head()) #skliausteliu viduje nurodyti kiek norime matyti eiluciu, tiek ir atvaizduos

# print(df['Name']) #atvaizduoja tik vardus

# selected_columns = df[['Name', 'City']]
# print(selected_columns) #atvaizduos tik tuos stulpelius kuriuos nurodeme

"""         prideti nauja stulpeli  """
# df['Salary'] = [1600, 1400, 1300, 1200]
# print(df)

"""         Gruojame duomenis pagal miesta ir gaukime vid. atlyginima"""
# average_salary_by_city = df.groupby('City') ['Salary'].mean() #butent mean veda vidurki
# print(average_salary_by_city)

"""          Ieskome vid. amziaus   """
# average_age = df['Age'].mean()
# print(f"Average age: {average_age}")

"""         filtruojame pagal nurodyta salyga   (siuo atveju metai)"""
# filtered_data = df[df['Age'] > 25][['Name', 'Age']] #dar pridejus skliaustelius atskirs name ir age
# print(filtered_data)



"""         darbas su employees.csv"""
df = pd.read_csv('employees.csv')
# print(df.head(5))

# gruopuojam pagal 'firrst_name' stulpeli ir suskaiciuoti jo dydi
group_sizes = df.groupby('FIRST_NAME').size() #size suskaiciuoja kiek yra zmoniu vienodais vardais
# print(group_sizes)

group_average = df.groupby('FIRST_NAME')['SALARY'].mean()
# print(group_average)

group_stats = df.groupby('FIRST_NAME')['SALARY'].describe() #describe sukuria statistika
# print(group_stats)

group_max = df.groupby('FIRST_NAME')['SALARY'].max() #atfiltruoja is visu vardu max atlyginimus
# print(group_max)

group_agg = df.groupby('FIRST_NAME').agg({'SALARY': ['sum', 'mean', 'max', 'size']}) #agreguoja suma, vidurki ir max algas ir dar size parodo kiek vardu buvo
# print(group_agg)


"""         atvaizduojam linijinne diagrama     """
# group_agg.plot(kind='line') #sukuriam linijine diagrama

# #pridedam diagramos antrastes
# plt.title('Suvestines statiska pagal vardus ir ju atlyginimus')
# plt.xlabel('Vardas')
# plt.ylabel('Atlyginimas')

# #atvaizduojam diagramoje
# plt.show()


#sukuriam 4 pie grafikus
# group_agg.plot(kind='pie', subplots=True, figsize=(8, 4)) 
# plt.show()


#sukuriam stulpeline diagrama
# group_agg.plot(kind='bar', figsize=(16, 4)) 
# plt.show()
