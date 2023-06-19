

# class Darbuotojas:
#     def __init__(self, vardas, pavarde, atlyginimas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.atlyginimas = atlyginimas
#         # parasyti metoda kuris padidins darbuotoju atlyginima tam tikru %
#     def padidinti_atlyginima(self, procentai):
#         padidinimas = self.atlyginimas * procentai / 100
#         self.atlyginimas += padidinimas

#     def pakeisti_pavarde(self, nauja_pavarde):
#         self.pavarde = nauja_pavarde
#         print("Pavarde pakeista sekmingai")

#     def visa_informacija(self):
#         print(f"informacija apie darbuotoja: ")
#         print(f"Vardas: {self.vardas}")
#         print(f"Pavarde: {self.pavarde}")
#         print(f"Atlyginimas: {self.atlyginimas}")

# Darbuotojas1 = Darbuotojas("Jonas", "Jonaitis", 1000)
# Darbuotojas2 = Darbuotojas("Petras", "Petraitis", 1200)

# Darbuotojas1.padidinti_atlyginima(10)
# print(f"{Darbuotojas1.vardas} {Darbuotojas1.pavarde} gavo Nauja atlyginima: {Darbuotojas1.atlyginimas}")

# Darbuotojas1.pakeisti_pavarde("Kazlauskas")
# print(f"{Darbuotojas1.vardas} {Darbuotojas1.pavarde} pasikeite pavarde!")

# Darbuotojas1.visa_informacija()



# Darbuotojas2.padidinti_atlyginima(10)
# print(f"{Darbuotojas2.vardas} {Darbuotojas2.pavarde} gavo Nauja atlyginima: {Darbuotojas2.atlyginimas}")



# class Preke:
#     def __init__(self, pavadinimas, kaina, kiekis):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.kiekis = kiekis
#         #parasyti metoda kuris atnaujina kaina
#     def atnaujinti_kaina(self, nauja_kaina):
#         self.kaina = nauja_kaina
#         print(f"{self.pavadinimas} nauja kaina ---> {nauja_kaina}")

#     def sandelio_likutis(self, pardavimo_kiekis):
#         if pardavimo_kiekis <= self.kiekis:
#             self.kiekis -= pardavimo_kiekis
#             print(f"{self.pavadinimas} buvo parduota: {pardavimo_kiekis} ")
#         else:
#             print(f"{self.pavadinimas} likutis nepakankamas")

#     def sandelio_papildymas(self, padidintas_likutis):
#         self.kiekis += padidintas_likutis
#         print(f"Padidintas {self.pavadinimas} Likutis: {padidintas_likutis}")


# Preke1 = Preke("Pienas", 1.45, 10)
# Preke1.atnaujinti_kaina(0.99)
# Preke1.sandelio_likutis(10)
# Preke1.sandelio_papildymas(10)
# print("sandelio likutis:", Preke1.kiekis)

# Preke2 = Preke("Duona", 2.39, 20)
# Preke2.atnaujinti_kaina(0.99)


# pranesti pirkejui, kad sandelyje neliko prekiu


