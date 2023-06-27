"""Sukurkite klasę "Mokinys", turinčią atributus "vardas", "pavarde" ir "pazymiai".

Parašykite metodą, kuris pridės naują pažymį prie mokinio pažymių sąrašo.

Parašykite metodą, kuris suskaičiuos mokinio pažymių vidurkį.

Sukurkite kelis objektus iš šios klasės su skirtingais pažymiais ir patikrinkite, ar vidurkis skaičiuojamas teisingai."""


class Mokinys:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pazymiai = []

    def prideti_pazymi(self, pazymys):
        self.pazymiai.append(pazymys)

    def skaiciuoti_vidurki(self):
        if len(self.pazymiai) == 0:
            return 0
    def suma_pazymiu = sum(self.pazymiai)
        if vidurkis = suma_pazymiu / len(self.pazymiai)
            return vidurkis


# Sukuriam kelis "Mokinys" objektus su skirtingais pažymiais
mokinys1 = Mokinys("Jonas", "Jonaitis")
mokinys1.prideti_pazymi(8)
mokinys1.prideti_pazymi(9)
mokinys1.prideti_pazymi(7)

mokinys2 = Mokinys("Petras", "Petraitis")
mokinys2.prideti_pazymi(10)
mokinys2.prideti_pazymi(9)
mokinys2.prideti_pazymi(8)

# Patikriname, ar vidurkis skaičiuojamas teisingai
vidurkis1 = mokinys1.skaiciuoti_vidurki()
vidurkis2 = mokinys2.skaiciuoti_vidurki()

print(f"{mokinys1.vardas} {mokinys1.pavarde} pažymių vidurkis: {vidurkis1}")
print(f"{mokinys2.vardas} {mokinys2.pavarde} pažymių vidurkis: {vidurkis2}")

""""init" metodas yra konstruktorius, kuris yra kviečiamas naują "Mokinys" objektą sukuriant. 
Jis priima du parametrus: "vardas" ir "pavarde". Šie parametrai nustato objekto atributus "vardas" ir "pavarde". 
Taip pat šiame metode yra sukuriamas tuščias sąrašas "pazymiai", skirtas saugoti mokinio pažymius.
"prideti_pazymi()" metodas leidžia pridėti naują pažymį į mokinio "pazymiai" sąrašą. 
Jis priima vieną parametrą - "pazymys" - ir naudoja "append()" metodą, kad pridėtų jį prie sąrašo.
"skaiciuoti_vidurki()" metodas skaičiuoja mokinio pažymių vidurkį. 
Metodas pradžioje patikrina, ar sąraše yra bent vienas pažymys (tikrina, ar "pazymiai" sąrašo ilgis yra didesnis už 0). 
Jei sąrašas tuščias, metodas grąžina 0. Jei sąrašas ne tuščias, jis naudoja "sum()" funkciją, 
kad suskaičiuotų visų pažymių sumą ir padalina ją iš sąrašo ilgio, norėdamas gauti vidurkio reikšmę. Galiausiai metodas grąžina vidurkį."""