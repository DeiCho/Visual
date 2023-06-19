# """Objektinis programavimas"""

# class Automobilis:
#     def __init__(self, spalva, greitis):
#         self.spalva = spalva
#         self.greitis = greitis
#         self.uzvesta = False

#     def automobilio_busena(self):
#         if not self.uzvesta:
#             print("Automobilis uzsivede")
#             self.uzvesta = True
#         else:
#             print("Automobilis jau uzvestas") 

#     def didinam_greiti(self, kiekis):
#         self.greitis += kiekis

#     def uzgesinam_varikli(self):
#         if self.uzvesta:
#             print("automobilis uzgeso")
#             self.uzvesta = False
#         else:
#             print("automobilis jau uzgesintas")



# honda = Automobilis("Juoda", 100)
# honda.automobilio_busena()
# honda.didinam_greiti(20)
# print(honda.greitis)
# honda.uzgesinam_varikli()
# # print("Jusu esamas greitis: ", honda.greitis)