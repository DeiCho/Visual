import numpy as np #kalba skirtau labiau skaiciavimams
import pandas as pd
import matplotlib.pyplot as plt


# sukuriama np array (masyva)
# arr = np.array([1, 2, 3])
# arr2 = np.array([ 4, 5, 6])
# result = arr + arr2
# print(result)


# arr = np.array([1, 2, 3, 4, 5])
# result = np.square(arr) 

#   indeksavimas
# value = arr[1]
# print(value)

#   array slicing
# sliced_arr = arr[1:4]
# print(sliced_arr) # parodys 2, 3, 4

# sliced_arr = arr[:3]
# print(sliced_arr) # parodys pirmas 3 reiksmes

# sliced_arr = arr[3:]
# print(sliced_arr) # parodys nuo 3 iki galo (kiek sarase nurodyta)


# matrica = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# matrica2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
# daugyba = np.dot(matrica, matrica2)
# print(daugyba)


# daugyba [0, 0] = (1*10) + (2*13) + (3*16) = 84



#   printinam random 5 skaicius
# random_numbers = np.random.randint(0, 10, size=5)
# print(random_numbers)


#   nuo 0 iki 1 atprintina 5 skaicius  (intervalas)
# numbers = np.linspace(0, 1, 5)
# print(numbers)



# generuoja skaiciu seka
# sequance = np.arange(10)
# print(sequance)

#   breziam sinuso grafika
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Sinusine funkcija')
# plt.show()



#   padeda random 100 tasku
# x = np.random.rand(100)
# y = np.random.rand(100)

# plt.scatter(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('random point')
# plt.show()


# generuojamo atsitiktiniai skaiciai ir nurodo butent ta skaiciu tam tikroje dimensijoje
# data = np.random.randn(1000)

# plt.hist(data, bins=20)
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histrogram')
# plt.show()


# printinam skaicius kurie sarase yra daugiau uz 2
# masyvas = np.array([1, 2, 3, 4, 5])

# daugiau_uz_du = masyvas[masyvas > 2]
# print(daugiau_uz_du)



# grazina indeksa (ne skaicius) 0-1; 1-2 t.t. siuo atveju uz 2 yra didesnis indeksas 2(3),3(4) ir 4(5)
# masyvas = np.array([1, 2, 3, 4, 5])

# daugiau_uz_du = np.where(masyvas > 2)
# print(daugiau_uz_du)


# logine seka grazina Falsa, False, True 
# arr1 = np.array([True, False, True])
# arr2 = np.array([False, True, True])
# result = np.logical_and(arr1, arr2)
# print(result)


# isskiria skaicius i dvi dalis po 3 skaiciaus
# arr = np.array([1, 2, 3, 4, 5, 6])
# change_arr = np.reshape( arr, (2, 3))
# print(change_arr)

# isskiria skaicius i 3 dalis
# arr = np.array([1, 2, 3, 4, 5, 6])
# splitting = np.split( arr, 3)
# print(splitting)


# surikiuoja skaicius
# arr = np.array([4, 1, 3, 5, 2, 6])
# sorting = np.sort(arr)
# print(sorting)


# isrikiuoja ir palieka tik unikalias reiksmes
# arr = np.array([4, 1, 1, 1, 3, 2, 5, 6, 3, 5, 2, 6])
# unique = np.unique(arr)
# print(unique)



"""         Akcijos         """

# akcijos = np.array([100, 110, 120, 115, 105, 95, 105, 100]) #duomenu sarasas su akciju kainu reiksmemis
# #apskaiciuojam dienos pelna ir nuostoli
# dienos_pelnas = akcijos[1:] - akcijos[:-1] #ima nuo pirmos iki paskutines dienos kainos
# dineos_nuostolis = akcijos[:-1] - akcijos[1:]

# # randame diena su didziausia ir maziausia dienis kaina
# didziausia_reiksme = np.max(akcijos)
# didziausios_reiksmes_indeksas = np.argmax(akcijos)

# maziausia_reiksme = np.min(akcijos)
# maziausios_reiksmes_indeksas = np.argmin(akcijos)


# #apskaiciuoja akcju kainos svyravima
# kainos_svyravimas = np.ptp(akcijos)

# print(f'Dienos pelnas: {dienos_pelnas}')
# print(f'Dienos nuostolis: {dineos_nuostolis}')
# print(f'Didziausia akciju kaina: {didziausia_reiksme}, dienos: {didziausios_reiksmes_indeksas +1}')
# print(f'Maziausia akciju kaina: {maziausia_reiksme}, dienos: {maziausios_reiksmes_indeksas +1}')

# print(f'Akciju dienos svyravimas: {kainos_svyravimas}')


# # piesiame linijine diagrama

# plt.plot(range(1, len(akcijos) +1), akcijos, marker='o')
# plt.title('Akciju kainos')
# plt.xlabel('Diena')
# plt.ylabel('Kaina')


# # Zymime didziausia ir maziausia kainas
# plt.plot(didziausios_reiksmes_indeksas +1, didziausia_reiksme, marker='o', color='green', label='Didiziausia')
# plt.plot(maziausios_reiksmes_indeksas +1, maziausia_reiksme, marker='o', color='red', label='Maziausia')

# # Rodyti legenda
# plt.legend()

# #Rodyti diagrama
# plt.show()



"""         Uzduotis su Temperatura         """

# temperaturos = np.array(
#     [20, 22, 23, 19, 15, 12, 10, 12, 35, 36, 35, 22, 25, 24, 26, 27, 29, 21, 18, 24, 23, 21])

#     #apskaiciuojame vid. temperatura
# vidutine_temp = np.mean(temperaturos)
# # print(vidutine_temp)

#     #apskaiciuojame didziausia temp.
# didziausia_temp = np.max(temperaturos)
#     #apskaiciuojame maziausia temp.
# maziausia_temp = np.min(temperaturos)

# df = pd.DataFrame({'Temperatura': temperaturos })
#     #nusibereziame temperaturos riba (pvz. nuo kuruios skaitome, kad karsta)
# slenkscio_verte = 23

# #     # ieskome dienu kai temp. virsijo riba
# # virsijo_slenkstine_temp = temperaturos[temperaturos > slenkscio_verte]
# # print(f'Dienos, kai temperatura virsijo slenkstine verte: {virsijo_slenkstine_temp}')


# filtruojame_df = df[df['Temperatura'] > slenkscio_verte]


# plt.plot(df.index, df['Temperatura'], label='Temperatura')
# plt.scatter(filtruojame_df.index, filtruojame_df['Temperatura'], color='red', label='Virsijo slenksti')
# plt.axhline(y=slenkscio_verte, color='gray', linestyle='--', label='Slenkscio verte')
# plt.xlabel('Dienos')
# plt.ylabel('Temperatura')
# plt.title('Dienine temperatura')
# plt.legend()
# plt.show()




