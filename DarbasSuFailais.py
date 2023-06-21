# Darbas su failasi naudojant open funkcija

# gali buti bet koks filas (txt, excelis t.t.) - "r" - read, skaito faila "w" - write, iraso tam tikras reiksmes

# file = open("failoPavadinimas.txt", "w")   
# content = file.write("Idedame teksta i nauja faila")#automatiskai suskure txt faila (kai naudojom file.write("idedame nauja teksta"))
# file = open("failoPavadinimas.txt", "r")  #nuskaito tai ka idejome i faila
# file = open("failoPavadinimas.txt", "a") # a - append, naudojama pakeisti teksta, naudojam su w - write
# file = open("failoPavadinimas.txt", "a", encoding="utf8") # leidzia naudoti lietuviskas raides
# content = file.write("naujas tesktas") 
# content.close()
# file = open("failoPavadinimas.txt", "a", encoding="utf8") # leidzia naudoti lietuviskas raides
# file.write("naujas tesktas") 
# file.close() #ipastina teksta ir uzdaro faila

# with open("failoPavadinimas2.txt", "w", encoding="utf8") as file:
#     file.write("Tekstas antrajame faile\n") # sukure nauja faila, kuriame nebereikia naudoti "close" funkcijos ir nebedubliuoja teksto, 
#     file.write("antra eilute\n") # \n - perkielia i kita eilute
#     file.write("trecia eilute")

# filename = input("Iveskite dailo pavadinima--> ")

# try:
#     with open(filename, "r", encoding="utf8") as file:
#         content = file.read()
#         print("File content: ")
#         print(content)
# except FileNotFoundError:
#     print("File were not found")
# except:
#     print("Something went wrong!") #perskaito sukurta faila, jeigu neranda - "file went wrong", jeigu randa bet nenuskaito "something went wrong"


# skuriam faila ir is karto paieskoje ji surandame ir perskaitome
# with open("tekstas.txt", "w", encoding="utf8") as file:
#     file.write("Tekstas tekstas.txt faile\n") 
#     file.write("antra eilute\n") 
#     file.write("trecia eilute")

# filename = input("Iveskite failo pavadinima--> ")

# try:
#     with open(filename, "r", encoding="utf8") as file:
#         content = file.read()
#         print("File content: ")
#         print(content)
# except FileNotFoundError:
#     print("File were not found")
# except:
#     print("Something went wrong!") #perskaito sukurta faila, jeigu neranda - "file went wrong", jeigu randa bet nenuskaito "something went wrong"


"""                     sukuriam faila ivedant pavadinime inpute ir iskarto iraso duomenis"""
# filename = input("iveskite naujo failo pavadinima --> ")
# try:
#     with open(filename, "w", encoding= "utf8") as file:
#         file.write("Pavyzdiniai duomenys: \n")
#         file.write("Vardas: Mantas\n")
#         file.write("Pavarde: Markus")
#         print("Duomenys sėkmingia įrašyti")
# except:
#     print("Ivyko klaida įrašant duomenis")





