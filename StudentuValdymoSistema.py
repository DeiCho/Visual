"""Objektinis programavimas"""

class Studentas:
    # Kuriamas konstruktorius
    def __init__(self):
        # sukuriamos tuscias masyvas(listas), kuriame talpinsime visus studentu numerius
        self.studentuSarasas = []

        #kuriame metoda "naujas studentas"

    def naujas_studentas(self, vardas, pavarde, studento_numeris):
        #inicijuojame saskaitos parametrus
        studento_info = {
            "vardas": vardas,
            "pavarde": pavarde,
            "studento_numeris": studento_numeris
            }
            # pridedame saskaita
        self.studentai.append(studento_info)
        print("Naujas studentas sekmingai sukurtas")

        #studento pridejimas
    def kito_studento_pridejiamas(self.studentuSarasas):
        naujas_sarasas = []
        for naujas_studentas in self.studentuSarasas:
            # jei studentas nerastas, pridesime prie naujo saraso
            if naujas_studentas not in naujas_sarasas:
                naujas_sarasas.append(naujas_studentas)
                print("Stundetas sekmingai pridetas")
                break
            else:
                print("Nepavyko prideti naujo studento!")

    def isemimas(self, studento_numeris):
        for naujas_studentas in self.studentuSarasas:
         #jei sutdentas rastas isimsime ji is saraso
            if naujas_studentas["studento_numeris"] == studento_numeris:
                print("Studentas sekmingai isimtas")
            else:
                print("Nepavyko rasti saskaitos su nuroytu numeriu!")

    def visas_sarasas(self, studento_numeris):
        for naujas_studentas in self.studentuSarasas:
            if saskaita["studento_numeris"] == saskaitos_numeris:
                print(f"Saskaitos Balansas: {saskaita['balansas']} €")
                break
            else:
                print("Nepavyko rasti saskaitos su nurodytu numeriu!")

#sukuriame objekta
vuSarasai = Studentas()

# naudojame while cikla ir leidziame klinetui pasirinkti norima operacija
while True:
     print("Pasirinkite norima operacija --> ")
     print("1. Sukurti nauja studenta")
     print("2. Ivesti studentuo duomenis")
     print("3. Isimti studenta is saraso")
     print("4. Patikrinti studentu sarasa")
     print("0. Baigti operacijas ")
     pasirinkimas = input("Iveskite pasirinkimo numeri -->" )
     
     #inicijuojame operacijas
     if pasirinkimas == "1":
          vardas = input("Iveskite varda --> ")
          pavarde = float(input("Iveskite pradini balansa --> "))
          numeris = input("Iveskite saskaitos numeri --> ")
          # gauname varda ir pradini balansa
          sebBankas.nauja_saskaita(vardas, pavarde, numeris)
     elif pasirinkimas == "2":
          numeris = input("Iveskite saskaitos numeri --> ")
          suma = float(input("Iveskite inesama suma --> "))
          sebBankas.balanso_didinimas(numeris, suma)
     elif pasirinkimas == "3":
          numeris = input("Iveskite saskaitos numeri --> ")
          suma = float(input("Iveskite isimama suma --> "))
          sebBankas.isemimas(numeris, suma)
     elif pasirinkimas == "4":
          numeris = input("Iveskite saskaitos numeri --> ")
          sebBankas.balansas(numeris)
     elif pasirinkimas == "0":
          break
     else:
          print("Neteisingas pasirinkimas! Bandykite dar karta.")