from colorama import init, Fore, Back, Style
import pandas as pd
import string
import random

"""         1. Parašykite funkciją, kuri priima tekstą ir grąžina žodžius, kurie pasikartoja daugiau nei vieną kartą. 
            Papildoma sąlyga žodžius turi grąžinti sąraše."""

# def pasikartojantys_zodziai(tekstas):
#     zodziai = tekstas.split()
#     sarasas = []
#     for zodis in set(zodziai): #set zodis atrinks unikalius, o kitus ides i sarasa
#         if zodziai.count(zodis) > 1:
#             sarasas.append(zodis)
#     return sarasas

# tekstas1 = "Labas rytas, Laba diena, Labas vakaras"
# print(pasikartojantys_zodziai(tekstas1)) #isprintina "Labas"

# def pasikartojantys_zodziai():
#     tekstas = input("Irasykite teksta: ")
#     zodziai = tekstas.split()
#     sarasas = []

#     for zodis in set(zodziai): #set zodis atrinks unikalius, o kitus ides i sarasa
#         if zodziai.count(zodis) > 1:
#             sarasas.append(zodis)

#     return sarasas

# print(pasikartojantys_zodziai)

"""     2. Parašykite funkciją, kuri nuskaito tekstiniame faile esančius žodžius ir grąžina juos surikiuotus pagal abėcėlę."""

# def surikiuoti_zodziai(failo_pavadinimas):
#     with open(failo_pavadinimas, "r", encoding="utf8") as file:
#         content = file.read()
#         text = content.split()
#         sorting = sorted(text)
#     return sorting

# failas = "tekstinis_failas.txt"
# print(surikiuoti_zodziai(failas))    


"""     3. Sukurti to do list aplikacija"""
# def menu():
#     print("1. Add task -->")
#     print("2. View tasks -->")
#     print("3. Mark task as completed -->")
#     print("4. Remove task -->")
#     print("5. Exit --> \n")

# def add_task(todo_list):
#     task = input("Enter task description: ")
#     todo_list.append({"task": task, "completed": False})
#     print("Task added successfully! \n")

# def view_task(todo_list):
#     if not todo_list:
#         print(Fore.RED+"Your to-do list is empty \n")
#     else:
#         print(Fore.GREEN+"Your to-do list: ")
#         for index, task in enumerate(todo_list, start=1):
#             status = "✓" if task["completed"] else " "
#             print(f"{index}. [{status}] {task['task']}")

# def mark_as_completed(todo_list):
#     view_task(todo_list)
#     task_number = int(input("Enter a number of the task you want to mark as completed -->")) - 1
#     if 0 <= task_number < len(todo_list):
#         todo_list[task_number]["completed"] = True
#         print("Task marked as completed! \n")
#     else:
#         print("Invalid task number!")

# def remove_task(todo_list):
#     view_task(todo_list)
#     task_number = int(input("Enter a number of the task you want to mark as completed -->")) - 1
#     if 0 <= task_number < len(todo_list):
#         removed_task = todo_list.pop(task_number)
#         print(f"Your task '{removed_task['task']}' was removed!")
#     else:
#         print("Invalid task numner!")

# def main():
#     todo_list = []
#     while True:
#         menu()
#         choice = input("Enter your choice (1-5): ")
#         if choice == "1":
#             add_task(todo_list)

#         elif choice == "2":
#             view_task(todo_list)
        
#         elif choice == "3":
#             mark_as_completed(todo_list)

#         elif choice == "4":
#             remove_task(todo_list)

#         elif choice == "5":
#             print("Exiting to-do list!")
#             break
#         else:
#             print("Wrong input!")

# if __name__ == '__main__':
#     main()

"""     4. programele kuri leidzia suvesti duomenis apie studentus       """

# def studentuo_duomenu_ivedimas():
#     studento_duomenys = pd.DataFrame(columns=['Vardas', 'Amzius', 'Pazymis'])

#     while True:
#         studento_vardas = input("Ivesktine stundento varda(or 'quit' to exit): ")
#         if studento_vardas.lower() == 'quit':
#             break
#         studento_amzius = int(input("Iveskite studento amziu: "))
#         studento_pazymis = int(input("Iveskite studento pazymi: "))

#         studento_duomenys = pd.concat([studento_duomenys, pd.DataFrame({
#             "Vardas": [studento_vardas],
#             "Amzius": [studento_amzius],
#             "Pazymis": [studento_pazymis]
#         })])


#     print("\n Studento Sarasas: \n")
#     print(studento_duomenys)
#     average_age = studento_duomenys['Amzius'].astype(int).mean()
#     avg_grade = studento_duomenys['Pazymis'].astype(int).mean()
#     print("\n Vidutinis amzius: ", average_age)
#     print("\n Vidutinis pazymis: ", avg_grade)

#     surikiuoti_duomenys = studento_duomenys.sort_values(by='Amzius', ascending=False)
#     print("\n Studento sarasa surikiuotas pagal pazymi: ")
#     print(surikiuoti_duomenys)

# studentuo_duomenu_ivedimas()

"""     5. kuriame Password generator   """

# def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
#     chars = ''
#     if include_uppercase:
#         chars += string.ascii_uppercase #ascii prideda kiekciena raide i chars lista

#     if include_lowercase:
#         chars += string.ascii_lowercase

#     if  include_numbers:
#         chars += string.digits

#     if include_special_chars:
#         chars += string.punctuation
#     if not chars:
#         print('Error: No character type selected for the password')
#         return None
    
#     password = ''.join(random.choice(chars) for _ in range(length))
#     return password

# def main():
#     print('Welcome To The Password Generator 3000!')
#     length = int(input('Choose your password length: '))
#     include_uppercase = input('Include UPPERCASE latters?(y/n): ').lower() == 'y'
#     include_lowercase = input('Include lowercase latters?(y/n): ').lower() == 'y'
#     include_numbers = input('Include numbers?(y/n): ').lower() == 'y'
#     include_special_chars = input('Include special characters?(y/n): ').lower() == 'y'

#     password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)
#     if password:
#         print('Generated password: ', password)
    
# if __name__ == '__main__':
#     main()

