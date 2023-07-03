import matplotlib.pyplot as plt
import seaborn as sns #papildo matplotliba ir padeda visualizuoti

#uzsikraunam pavizdinius duomenis
# data = sns.load_dataset('iris') #1
# data = sns.load_dataset('tips') #2
# data = sns.load_dataset('diamonds')



#stiliaus pasirinkimas/nustatymas
# sns.set_style('whitegrid')

#braizome stulpeline diagrama

# sns.barplot(x='species', y='sepal_length', data=data)#1
# sns.barplot(x='total_bill', y='tip', data=data) #2
# sns.scatterplot(x='total_bill', y='tip', data=data) #2 sklaidos diagrama
# sns.lineplot(x='total_bill', y='tip', data=data) #2
# sns.histplot(x='total_bill', data=data) #2
# sns.boxplot(x='day', y='total_bill', data=data) #candlesticks

# numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns #2
# koreliacija = data[numeric_cols].corr() #2
# sns.heatmap(koreliacija, annot=True, cmap='coolwarm') #2
# sns.violinplot(x='day', y='total_bill', data=data) #2
# sns.pairplot(data) #pavaizduoja daug lenteliu #2



# data = sns.load_dataset('diamonds')
# column_names = data.columns #pasiziurim kokie yra stulpeliai datasete
# print(column_names)

# data = sns.load_dataset('diamonds')
# obj = sns.FacetGrid(data, col='cut') #facegrid nurodo sulpeli pagal kuri grupuojam
# obj.map(sns.histplot, 'carat')

# sns.scatterplot(x='carat', y='price', data=data)

# diagramos pavadinimas/antraste
# plt.title('tips by total bill')

# plt.show()


#sukurti barplot kuriame butu atvaizduoti cut(x) ir color vid.price (y) reiksmiu stulpeliai
# sns.barplot(x='cut', y='price', hue='color', errorbar=None, data=data) #hue naudoja spalvas grupavimui
# plt.show()

#ismeta pagal pjuvio tiksluma:
# objektas = sns.FacetGrid(data, hue='color', col='cut')
# objektas.map(sns.barplot, 'carat', 'price')
# plt.show()

#isanalizuoti kaip keiciasi isgyvenusiuju skaicius pagal klase (titanike)
# data = sns.load_dataset('titanic')
# survived = data['pclass'][data['survived']==1].value_counts().sort_index()
# # print(data)
# total_survived = data['survived'].sum()

# sns.barplot(x=survived.index, y=survived.values)
# for i, count in enumerate(survived.values):
#     plt.text(i, count, str(count), ha='center', va='bottom')
# plt.xlabel('Keliones klase')
# plt.ylabel('Isgyvenusiuju skaicius')
# plt.title('Isgyvenusiuju skaicius, pagal klase')
# # plt.yticks(range(0, 15, 5))
# plt.show()


