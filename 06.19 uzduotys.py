""" 1.Parašykite programą, kuri atspausdina visus lyginius skaičius nuo 1 iki 10."""
# sarasas = range(1,11)
# for skaicius in sarasas:
#     if skaicius % 2 == 0:
#         print(skaicius)

                        # arba 

# for skaicius in range (2, 11, 2) # nuo 2 skciaus printina kas antra skaiciu (siuo atvieju visus lyginius)



""" 2. Sukurkite sąrašą, kuriame yra keletas skaičių. Naudojant for ciklą, apskaičiuokite sąrašo skaičių sumą"""
# def saraso_suma(sarasas):
#     suma = 0
#     for visi_skaiciai in sarasas:
#         if visi_skaiciai > 0:
#           suma += visi_skaiciai
#     return suma

# sarasas = range(1, 11)
# rezultatas = saraso_suma(sarasas)
# print(rezultatas)

# arba
# sarasas = [5, 3, 8, 2, 9]
# suma = 0
# for skaicius in sarasas:
#    suma += skaicius
# print ("Saraso suma: ", suma)


""" 3. Parašykite programą, kuri atspausdina visus skaičius nuo 1 iki 20, tačiau jei skaičius yra dalijamas iš 3, 
atspausdinkite "Fizz", jei skaičius yra dalijamas iš 5, atspausdinkite "Buzz","""

# for skaicius in range(1,21):
#     if skaicius % 3 == 0 and skaicius % 5 == 0:
#         print("FizzBuzz")
#     elif skaicius % 3 == 0:
#         print("Fizz")
#     elif skaicius % 5 == 0:
#         print("Buzz")
  
"""4.Sukurkite klasę "KnygosBiblioteka", turinčią atributą "knygos" (sąrašą) ir metodus "pridėti_knygą" ir "rodyti_knygas". 
Pridėkite funkcionalumą, kad galėtumėte pridėti knygas į sąrašą ir atspausdinti visas bibliotekoje esančias knygas."""

# class KnygosBiblioteka:
#     def __init__(self):
#         self.knygos = []
    
#     def prideti_knyga(self, knyga):
#         self.knygos.append(knyga)
#         print(f"Knyga: {knyga} - prideta sekmingai")

#     def rodyti_knygas(self):
#         if self.knygos:
#             print("Knygos bibliotekoje: ")
#             print()
#             for knyga in self.knygos:
#                 print(knyga)
#         else:
#             print("Biblioteka tuscia!")

# knyga = KnygosBiblioteka()
# print()
# knyga.prideti_knyga("Vienas lauke ne karys")
# knyga.prideti_knyga("O gal ir karys")
# print()
# knyga.rodyti_knygas()
# print()
# print(knyga)



"""5.Sukurkite žodyną su prekių pavadinimais ir jų kainomis. Parašykite programą, kuri suskaičiuoja ir atspausdina visų prekių kainų sumą."""

# prekes = {
#     "Obuolys": 0.99,
#     "Vynuoges": 7.99,
#     "Bananai": 3.99,
#     "Kivis": 0.55
# }
# suma = 0
# for kaina in prekes.values():
#     suma += kaina

# print(f"Visu prekiu suma: {suma}")


""" Atspausdinti is * trikampi """
# aukstis = 5
# eilutes = aukstis + 1
# for i in range(1, eilutes + 1): #kiekvienam zingsnyje ima nauja eilute iki 5
#     print(" " * (eilutes - i), end="") #printina tiek tarpu kiek yra eiluciu
#     print("*" * (2 * i - 1))    
# print(" " * (eilutes - 1), end="")
# print("|") #padaugina tarpus is 5 (eulute -1) t.y. 5+1-1