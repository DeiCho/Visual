# """Objektinis programavimas"""

# class Bankas:
#     # Kuriamas konstruktorius
#     def __init__(self):
#         # sukuriamos tuscias masyvas(listas), kuriame talpinsime visas banko saskaitas
#         self.saskaitos = []

#         #kuriame metoda "nauja saskaita"

#     def nauja_saskaita(self, vardas, pradinis_balansas, numeris):
#         #inicijuojame saskaitos parametrus
#         saskaita = {
#             "vardas": vardas,
#             "balansas": pradinis_balansas,
#             "numeris": numeris
#             }
#             # pridedame saskaita
#         self.saskaitos.append(saskaita)
#         print("Nauja saskaita sekmingai sukurta")

#         #balanso didinimas
#     def balanso_didinimas(self, saskaitos_numeris, suma):
#         #iteruosime(eisim per visas saskaitas) visas saskaitas ir atrasime musu saskaita kurioje norime padidinti balansa
#         for saskaita in self.saskaitos:
#             # jei saskaita rasta, padidinsime jos balansa
#             if saskaita["numeris"] == saskaitos_numeris:
#                 saskaita["balansas"] += suma
#                 print("Balansas sekmingai papildytas")
#             break
#         else:
#             print("Nepavyko rasti saskaitos su nurodytu numeriu!")

#     def isemimas(self, saskaitos_numeris, suma):
#         for saskaita in self.saskaitos:
#          #jei saskaita rasta isimsime pinigus
#             if saskaita["numeris"] == saskaitos_numeris:
#                 if saskaita["balansas"] >= suma:
#                     saskaita["balansas"] -= suma
#                     print("Pinigai sekmingai isimti")
#             else:
#                     print("Nepakankamas likutis")
#             break
#         else:
#             print("Nepavyko rasti saskaitos su nuroytu numeriu!")

#     def balansas(self, saskaitos_numeris):
#         for saskaita in self.saskaitos:
#             if saskaita["numeris"] == saskaitos_numeris:
#                 print(f"Saskaitos Balansas: {saskaita['balansas']} €")
#                 break
#             else:
#                 print("Nepavyko rasti saskaitos su nurodytu numeriu!")

# #sukuriame objekta
# sebBankas = Bankas()

# # naudojame while cikla ir leidziame klinetui pasirinkti norima operacija
# while True:
#      print("Pasirinkite norima operacija --> ")
#      print("1. Sukurti nauja saskaita")
#      print("2. Inesti pinigu i saskaita")
#      print("3. Isimti pinigus is saskaitos")
#      print("4. Patikrinti saskaitos likuti")
#      print("0. Baigti operacijas ")
#      pasirinkimas = input("Iveskite pasirinkimo numeri -->" )
     
#      #inicijuojame operacijas
#      if pasirinkimas == "1":
#           vardas = input("Iveskite varda --> ")
#           pradinis_balansas = float(input("Iveskite pradini balansa --> "))
#           numeris = input("Iveskite saskaitos numeri --> ")
#           # gauname varda ir pradini balansa
#           sebBankas.nauja_saskaita(vardas, pradinis_balansas, numeris)
#      elif pasirinkimas == "2":
#           numeris = input("Iveskite saskaitos numeri --> ")
#           suma = float(input("Iveskite inesama suma --> "))
#           sebBankas.balanso_didinimas(numeris, suma)
#      elif pasirinkimas == "3":
#           numeris = input("Iveskite saskaitos numeri --> ")
#           suma = float(input("Iveskite isimama suma --> "))
#           sebBankas.isemimas(numeris, suma)
#      elif pasirinkimas == "4":
#           numeris = input("Iveskite saskaitos numeri --> ")
#           sebBankas.balansas(numeris)
#      elif pasirinkimas == "0":
#           break
#      else:
#           print("Neteisingas pasirinkimas! Bandykite dar karta.")