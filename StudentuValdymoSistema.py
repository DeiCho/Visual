class Studentas:
    def __init__(self, studento_id, vardas, pavarde):
        self.studento_id = studento_id
        self.vardas = vardas
        self.pavarde = pavarde

class StudentuValdymoSistema:
    def __init__(self):
        self.studentai = []

    def prideti_studenta(self, studento_id, vardas, pavarde):
        studentas = Studentas(studento_id, vardas, pavarde)
        self.studentai.append(studentas)
        print(f"Studentas '{vardas} {pavarde}' pridėtas.")

    def pasalinti_studenta(self, studento_id):
        for studentas in self.studentai:
            if studentas.studento_id == studento_id:
                self.studentai.remove(studentas)
                print(f"Studentas '{studentas.vardas} {studentas.pavarde}' pašalintas.")
            return
        print("Studentas su tokiu ID nerastas.")

    def gauti_studenta_pagal_id(self, studento_id):
        for studentas in self.studentai:
            if studentas.studento_id == studento_id:
                return studentas
        return None

    def rodyti_studentus(self):
        print("Visi studentai:")
        for studentas in self.studentai:
            print(f"ID: {studentas.studento_id}, Vardas: {studentas.vardas}, Pavardė: {studentas.pavarde}")

# Sukuriam studentų valdymo sistemos objektą
sistema = StudentuValdymoSistema()

# Meniu
while True:
    print("Studentų valdymo sistema")
    print("1. Pridėti naują studentą")
    print("2. Pašalinti studentą")
    print("3. Gauti informaciją apie studentą pagal ID")
    print("4. Rodyti visus studentus")
    print("5. Baigti programą")

    pasirinkimas = input("Įveskite pasirinkimo numerį: ")

    if pasirinkimas == "1":
        studento_id = input("Įveskite studento ID: ")
        vardas = input("Įveskite studento vardą: ")
        pavarde = input("Įveskite studento pavardę: ")
        sistema.prideti_studenta(studento_id, vardas, pavarde)
    elif pasirinkimas == "2":
        studento_id = input("Įveskite studento ID: ")
        sistema.pasalinti_studenta(studento_id)
    elif pasirinkimas == "3":
        studento_id = input("Įveskite studento ID: ")
        studentas = sistema.gauti_studenta_pagal_id(studento_id)
        if studentas:
            print(f"Studentas: {studentas.vardas} {studentas.pavarde}")
        else:
            print("Studentas su tokiu ID nerastas.")
    elif pasirinkimas == "4":
        sistema.rodyti_studentus()
    elif pasirinkimas == "5":
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")

print("Programa baigta.")


"""
1.Sukuriamos dvi klases: Studentas ir StudentuValdymoSistema.

2.Studentas klasė turi tris atributus: studento_id, vardas ir pavarde. Jie nurodomi konstruktoriuje __init__() ir priskiriami objekto kintamiesiems.

3.StudentuValdymoSistema klasė turi vieną atributą studentai, kuris yra sąrašas, skirtas saugoti visus studentus. Jis inicijuojamas tuščiu sąrašu konstruktoriuje.

4.StudentuValdymoSistema klasė taip pat turi kelis metodus:

prideti_studenta() metodas priima studento informaciją (ID, vardą, pavardę), sukuria naują Studentas objektą ir prideda jį į studentai sąrašą.
pasalinti_studenta() metodas priima studento ID ir ieško studento sąraše. Jei randa studentą, jį pašalina iš sąrašo.
gauti_studenta_pagal_id() metodas priima studento ID ir ieško studento sąraše. Jei randa studentą, jį grąžina, kitu atveju grąžina None.
rodyti_studentus() metodas atspausdina visus studentus esančius studentai sąraše.

5.Sukuriamas StudentuValdymoSistema objektas vardu sistema.

6.Įgyvendinamas meniu, kuris leidžia vartotojui pasirinkti veiksmą:

Pasirinkus "1", vartotojas įveda studento informaciją, kuri yra perduodama prideti_studenta() metodui.
Pasirinkus "2", vartotojas įveda studento ID, kuris yra perduodamas pasalinti_studenta() metodui.
Pasirinkus "3", vartotojas įveda studento ID, kuris yra perduodamas gauti_studenta_pagal_id() metodui. Jei studentas rastas, atspausdinama jo informacija, kitu atveju pranešimas, kad studentas su tokiu ID nerastas.
Pasirinkus "4", iškviečiamas rodyti_studentus() metodas, kad atspausdintų visus studentus.
Pasirinkus "5", programa baigia darbą.

7.Programa vykdo pasirinkimą, kol vartotojas pasirenka "5" baigti programą."""