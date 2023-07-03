"""cikit-learn is an open source data analysis library, and the gold standard for Machine Learning (ML) in the Python ecosystem. 
Key concepts and features include: 
    Algorithmic decision-making methods, including: 
        Classification: identifying and categorizing data based on patterns."""

# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt 


# """Klusterizavimui"""
# from sklearn.datasets import make_blobs
# from sklearn.cluster import KMeans
# from sklearn.metrics import silhouette_score


"""Tiesine Regresija"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# iris = load_iris() #ikeliam duomenu rinkini
# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42) #padalinam domenis i mokymo ir testavo rinkinius

# knn = KNeighborsClassifier(n_neighbors=3) #sukurtas klasifikatorius su artimiausia 3 kaimynais
# # print(iris)

#   #treniruojamas klasifikatorius
# knn.fit(X_train, y_train)

#   #prgonozuojami rezultatai
# y_pred = knn.predict(X_test)

#   # ivertinamas tikslumas
# accuracy = accuracy_score(y_test, y_pred)
# print('Tikslumas: ', accuracy)

"""     Klusterizavimas     """

# #   sugeneroujami duomenys 
# x,y = make_blobs(n_samples=100, n_features=2, centers=3, random_state=42)

# #   inicijuojamas klasterizavimo modelis(musu atveju K-means)
# kmeans = KMeans(n_clusters=3, n_init='auto')

# #   priskiriame duomensis klasteriams
# labels = kmeans.fit_predict(x)

# #   ivertiname klasterizavimo rezultatus
# silhouette = silhouette_score(x, labels)
# print(silhouette)

"""Tiesine Regresija"""

# data = {
#     'X' : [1, 2, 3, 4, 5],
#     'Y' : [2, 4, 5, 4, 5]
# }

# df = pd.DataFrame(data)
# X = df[['X']]
# y = df['Y']

# #   inicijuojame tiesines regresijos modelis
# model = LinearRegression()
# model.fit(X, y)
# y_pred = model.predict(X)
# print('Nuokrypis:', model.intercept_)
# print('Koeficientas:', model.coef_)
# sns.regplot(x='X', y='Y', data=df)
# plt.show()

# data = sns.load_dataset('diamonds')
# X = data[['carat', 'depth', 'table']]
# y = data['price']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# #   Ivertiname modelio tiksluma naudojant vidutini kvadratini nuoktypi
# mse = mean_squared_error(y_test, y_pred)
# print("Vidutinis kvadtatinis nuokrypis (MSE): ", mse)

# #   atvaizduojame prognozes ir tikras reksmes naudojant regresijos diagrama
# df = pd.DataFrame({'Predicted price': y_pred, 'Actual price': y_test})
# sns.regplot(x='Actual price', y='Predicted price', data=df)
# plt.show()