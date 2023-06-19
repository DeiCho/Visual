# komentuoja viena eilute
"""
su 3 kabutem (is abieju pusiu) 
tiek eiluciu 
kiek reikia
"""


# vardas = "Deividas"
# amzius = 24

# arVartotojasAktyvus = False

"""'bool' nusako kad yra true/flase kintamsis"""
# produktoKaina = 3.99
# 'float' reiskia - per kableli
# print(type(amzius))
"""su "type" galima pasitikrinti kokio formato yra kintamasis vardas/amzius pvz: tekstas ar skaicius"""

# miestai = ["Vilnius", "Kaunas", "Klaipeda"]

#parodys 'list'
# print(type(miestai))
# print(miestai[0])  - grazins pirma reiksme (indeksavimas prasideda nuo 0)
# print(miestai[-1])
# miestai[1] = "Siauliai"
# pervadina Kauna i Siaulius
# miestai.append("Panevezys")
# itraukia panevezi gale
# miestai.insert(1, "Anyksciai")
# prideda anykscius priesais Kauna ir pastumia skaiciu seka
# miestai.pop()
# pop istrina paskutini kintamaji
# del miestai[2]
# istrina 3 miesta
# print(miestai)


# miestai = ["Vilnius", "Kaunas", "Klaipeda"]
# print("Mano vardas " + vardas + " As gyvenu " + miestai[0] + " mano amzius " + str(amzius))



"""----------------- su if"""
# vardas = "Deividas"
# amzius = 27
# miestai = ["Vilnius", "Kaunas", "Klaipeda"]

# if amzius == 18:
#     print("Pilnametis")

# elif amzius >= 25:                
"""galima daug elif prirasyt (daug salygu) iki kol grazina (siuo atveju) neigiama reiksme - nepilnametis"""
#     print("Daugiau nei 18")
# else:
#     print("Nepilnametis")

"""----------------- su if"""

# miestai = ["Vilnius", "Kaunas", "Klaipeda"]
# print(len(miestai)) 
"""parodo kiek yea miestu"""



# skiuciuSarasas = [1, 3, 5, 41, 55, 66, 77]
# if len(skiuciuSarasas) > 0:
#     print("Skaiciu saras pilnas")
# else:
#     print("Skaiciu sarasas tuscias")
"""patikrino ar sarase yra bent 1 reiksme"""



# zodis = "Kaunas"
# miestai = ["Vilnius", "Kaunas", "Klaipeda"]

# if zodis in miestai:
#     print("Zodis " + zodis + " egzistuoja sarase")

# else:
#     print("Zodis nerastas")
"""patikrino ar zodis "Kaunas" yra sarase"""


# zodis = "Kaunas"
# miestai = ["Vilnius", "Kaunas", "Klaipeda"]
# skiuciuSarasas = [1, 3, 5, 41, 55, 66, 77]
# skaicius = int(input("Iveskite skaiciu: "))

# if skaicius > 0:
#     print("Skaicius yra teigiamas")
# elif skaicius < 0:
#     print("Skaicius yra neigiamas")
# else:
#     print("Skaicius yra nulis")
"""sukureme mini masinele kuri tikrintu po "run" ar skaicius teigiamas/neigiamas/nulis"""


"""1.Patikrinkite, ar studentas išlaikė egzaminą."""
# ivertinimas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# islaikymoRiba = 5
# ivertinimas = int(input("Iveskite ivertinima: "))
# if ivertinimas >= islaikymoRiba:
#     print("Egzaminas islaikytas")
# else:
#     print("Egzaminas neislaikytas")

"""2.Patikrinkite, ar skaičius yra lyginis"""
# Skaiciai = 7
# if Skaiciai % 2 == 0:
#     print("Lyginis skaicius")
# else:
#     print("Nelyginis skaicius")

"""3. Patikrinkite, ar sąraše yra bent du skaičiai"""
# sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# if len(sarasas) >= 2:
#     print("yra 2 skaiciai")
# else:
#     print("nera 2 skaiciu")

# for i in range(1,11): 
#     print(i)
"""isspausdina nuo 1 iki 10 (11 nera nes neimtinai)"""


# vardai = ["Jonas", "Petras", "Aloyzas", "Martynas"]

# for vardas in vardai:
#     print(vardas)
"""isspausdina visus vardus (11 nera nes neimtinai)"""

# skaiciai = [10, 20, 30, 40, 50, 27]
# atrinkti = []

# for skaicius in skaiciai:
#     if skaicius > 27:
#         atrinkti.append(skaicius)
# print("Atrinkti skaiciai: ", atrinkti)
"""su append pridedam skaicius i eilute "atrinkti"""


# skaiciai = [10, 10, 20, 30, 40, 50, 27, 2, 5, 30, 99, 11]
# unikaliosReiksmes = []

# for skaicius in skaiciai:
#     if skaicius not in unikaliosReiksmes:
#         unikaliosReiksmes.append(skaicius)
# print("Unikalios reiksmes", unikaliosReiksmes)
"""su append pridedam skaicius i eilute "unikalios reiksmes" ir deda i unikalias is eiles"""


# def suma(a, b):
#     return a + b 
# rezultatas = suma(2, 5)
# print("Suma: ", rezultatas)
"""def pasako kad tai bus funkcija"""

# def pasisveikinimas(vardas = "anonimas"):
#     print("Labas, ", vardas)
# pasisveikinimas()
"""ka irasysi prie pasisveikinimo ta grazins "Labas, vardas", jei nieko neirasysi grazins "Labas, anonimas"""

# def sujungti_sarasus(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas

# rezultatas = sujungti_sarasus([1, 2, 3,], [4, 5, 6])
# print("sujungtas sarasas: ", rezultatas)


"""1.Parašykite funkciją 
ar_lyginis, kuri priima vieną skaičių kaip argumentą ir patikrina, ar skaičius yra lyginis. 
Jei skaičius yra lyginis, tada funkcija turi grąžinti True, o jei nelyginis - False."""

# def ar_lyginis(skaicius):
#     if skaicius % 2 == 0:
#         return True
#     else:
#         return False
# print(ar_lyginis(9))


"""2. Parašykite funkciją didziausias_skaicius, kuri priima sąrašą skaičių ir grąžina didžiausią skaičių iš sąrašo"""

# def didziausias_skaicius(sarasas):
#     didziausias = sarasas[0]
#     for skaicius in sarasas:
#         if skaicius > didziausias:
#             didziausias = skaicius
#     return didziausias

# skaiciuSarasas = [12, 6, 7, 8, 9, 1, 6, 54, 44]
# rezultatas = didziausias_skaicius(skaiciuSarasas)
# print(rezultatas)
"""0 nurodo pirma skaiciu (1), nuo kurio pradeda lyginti tarpusavy is eiles, prisimenant didziausia paskutini skaiciu"""

"""3. Parašykite funkciją unikalios_reiksmes, kuri priima sąrašą ir grąžina naują sąrašą, kuriame yra tik unikalios reikšmės iš pradinio sąrašo."""

# def unikalios_reiksmes(sarasas):
#     tuscias_sarasas = []
#     for reiksme in sarasas:
#         if reiksme not in tuscias_sarasas:
#             tuscias_sarasas.append(reiksme)

#     return tuscias_sarasas
# naujas_sarasas = [1, 1, 5, 6, 6, 6, 84, 95, 32, 32, 15]
# print(unikalios_reiksmes(naujas_sarasas))

"""Namu darbai"""
"""1.Apskaičiuokite skaičių sąrašo suma, išskyrus tuos skaičius, kurie yra lyginiai. 
Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina sumą."""

# def nelyginiu_suma(sarasas):
#     suma = 0
#     for nelyginis_skaicius in sarasas:
#         if nelyginis_skaicius % 2 != 0:
#           suma += nelyginis_skaicius
#     return suma

# sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rezultatas = nelyginiu_suma(sarasas)
# print(rezultatas)   

"""3.Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis skaičius."""

# def pirminis_skaicius(skaicius):
#     if skaicius < 2:
#         return False
#     for daliklis in range(2, skaicius):
#         if skaicius % daliklis == 0:
#             return False
#     return True
# skaicius = 13
# if pirminis_skaicius(skaicius):
#     print(f"skaicius {skaicius}, yra pirminis skaicius")
# else:
#     print(f"skaicius {skaicius}, nera pirminis skaicius")


""""funkcija while"""

# skaicius = 1
# while skaicius <= 5:
#     print(skaicius)
#     skaicius += 1
"""printina skaiciu +1 iki 5"""

"""paprasyti vartotojo ivesti skaiciu ir atspausdinti visus lyginius skaicius nuo ivesto skaiciaus iki 0 """
# skaicius = int(input("Iveskite skaiciu: "))
# while skaicius >= 0:
#     if skaicius % 2 == 0:
#         print(skaicius)
#     skaicius -= 1

