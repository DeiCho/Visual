""" randomizer"""

import random
import time



studentai = ["Rugile", "Egidijus", "Deividas", "Tomas", "Migle", "SauliusS", "SauliusA", 
             "Vaidas", "Ausrine", "Jurate", "Mantas", "Modestas"]
random_student = random.choice(studentai)

time.sleep(5)
print("Atsitiktinai pasirinktas studentas: ", random_student)
