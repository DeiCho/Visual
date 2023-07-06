import pandas as pd
import matplotlib.pyplot as plt
from students_db import create_table, insert_query, db_params

"""1. Užduotis:
     [+] Sukurkite klasę "Automobilis" su savybėmis "marke" ir "metai". 
     [+] Sukurkite metodą "informacija", kuris išveda automobilio informaciją.
     [+] Sukurkite vaikinę klasę "ElektrinisAutomobilis", kuri paveldi klasę "Automobilis" 
     ir papildomai turi savybę "baterijos_talpa" ir metodą "baterijos talpa informacija", 
     kuris išveda informaciją apie automobilio baterijos talpą."""

# class Automobilis:
#     def __init__(self, marke, metai):
#         self.marke = marke
#         self.metai = metai
        
#     def informacija(self):    
#         print(f"Automobilio marke yra: {self.marke}")
#         print(f"Automobilio pagaminimo metai yra: {self.metai}")
   
# class Elektromobilis(Automobilis):
#     def __init__(self,marke, metai, baterijos_talpa):
#         super().__init__(marke, metai)
#         self.baterijos_talpa = baterijos_talpa

#     def informacija(self):
#         super().informacija()
#         print(f"Elektromonilio baterijos talpa: {self.baterijos_talpa}")


# automobilis = Automobilis("Audi", "A6")
# elektromobilis = Elektromobilis("Tesla", "Model_X", "100kWH")

# automobilis.informacija() 
# print()
# elektromobilis.informacija()

"""2. Užduotis:
     [+] Naudodami pandas, nuskaitykite CSV failą "duomenys.csv" ir įrašykite duomenis į PostgreSQL 
     duomenų bazės "students" lentelę.
     [+] Papildoma sąlyga: Įrašykite duomenis į "students" lentelę tik tuomet, jei amžius yra didesnis nei 20."""

def load_data():
     data = pd.read_csv('duomenys.csv')
     filtered_data = data[data['amzius'] > 20]
     df = pd.DataFrame(filtered_data)
     return df


create_table()
insert_query()
