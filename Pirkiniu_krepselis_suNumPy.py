# import numpy as np 
# import pandas as pd
# import matplotlib.pyplot as plt

# """Apsirašykite duomenų rinkinį su pirkinių krepšelio prekių ir jų kainų informacija. 
# Naudodami NumPy ir Matplotlib: 
# Apskaičiuokite bendrą pirkinių krepšelio sumą. Raskite brangiausią ir pigiausią prekę. 
# Sudarykite pie diagramą, kurioje rodomi skirtingų prekių dalis bendroje sumoje."""

# prekes = np.array(['Burokeliai', 'Kefyras', 'Kiausiniai', 'Agurkai'])
# kaina = np.array([5.99, 2.99, 1.99, 0.99])
# kiekis = np.array([3, 1, 10, 7])


# didziausia_kaina = prekes[np.argmax(kaina)]
# print(didziausia_kaina)
# maziausia_kaina = prekes[np.argmin(kaina)]
# print(maziausia_kaina)

# fig, ax = plt.subplots()
# ax.pie(kaina * kiekis, labels=prekes, autopct='%1.1f%%', startangle=90) #%1.1f%% (formatavimas) nurodo kad bus 1sk po kablelio ir su % zenklu
# ax.axis('equal')

# plt.title('Prekiu krepselis pagal kainas')
# plt.show()