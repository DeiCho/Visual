# import colorama
# from colorama import Fore, Style
# colorama.init()


# class Skaiciuotuvas:
#     def __init__(self):
#         self.result = 100
        
#     def sudetis(self, skaicius):
#         self.result += skaicius

#     def atimtis(self, skaicius):
#         self.result -= skaicius

#     def daugyba(self, skaicius):
#         self.result *= skaicius

#     def dalyba(self, skaicius):
#         if skaicius != 0:
#             self.result /= skaicius
#         else:
#             print("Dalyba is nulio negalima")
        
#     def clear(self):
#         self.result = 0


#     def get_result(self):
#         return self.result

# skaiciuoklis = Skaiciuotuvas()
# while True:
#     print("Pasirinkite norima veiksma -> ")
#     print("1. Sudetis")
#     print("2. Atimtis")
#     print("3. Daugyba")
#     print("4. Dalyba")
#     print("0. Clear")
#     pasirinkimas = input("Iveskite pasirinkimo numeri -->" )

#     if  pasirinkimas == "1":
#         skaicius = int(input("Iveskite skaicu --> "))
#         skaiciuoklis.sudetis(skaicius)
#         #kadangi neturejom print, reikia "getteriu ir setteriu", kurie grazintu suskaiciuota reiksme, set metodas nustato reiksme, get - gauna reiksme
    
#     elif pasirinkimas == "2":
#         skaicius = int(input("Iveskite skaicu --> "))
#         # colour_input = Fore.RED + str(skaicius) + Style.RESET_ALL --> turetu nuspalvinti raudonai
#         skaiciuoklis.atimtis(skaicius)

#     elif pasirinkimas == "3":
#         skaicius = int(input("Iveskite skaicu --> "))
#         skaiciuoklis.daugyba(skaicius)

#     elif pasirinkimas == "4":
#         skaicius = int(input("Iveskite skaicu --> "))
#         skaiciuoklis.dalyba(skaicius)

#     elif pasirinkimas == "0":
#          skaiciuoklis.clear()
    
#     else:
#         print("Negalimas veiksmas")

#     print("Result: ", Fore.GREEN +  str(skaiciuoklis.get_result()) + Style.RESET_ALL)
#     print()