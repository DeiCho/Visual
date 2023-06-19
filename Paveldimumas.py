

#metodo perrasymas
# class Animal:
#     def make_sound(self):
#         print("The animal makes a sound")



# class Dog(Animal):
#     def make_sound(self):
#         print("The dog barks")


# dog = Dog()
# dog.make_sound()



"""              classes paveldimas             """
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand


#     def start_engine(self):
#         print("Engine started!")

#     def stop_engine(self):
#         print("Engine stopped!")

# class Car(Vehicle):

#     def drive(self):
#         print("Car is driving!")


# car = Car("Toyota")
# print(car.brand)
# car.start_engine()
# car.drive()
# car.stop_engine()





"""          Kitas pvz kaip vaikine classe perima savybes is tevines classes"""
# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def make_sound(self):
#         print("The animal makes a sound")

# class Dog(Animal):
#     def __init__(self,name, age):
#         # super paima savybes is tevines classes (name,....,.....)
#         super().__init__(name)
#         self.age = age

#     def make_sound(self):
#         print("The dog barks")


# dog = Dog("Bobby", 5)
# dog.make_sound()
# print(f"My dogs name is {dog.name}" + "and age is " + str(dog.age))




"""            sukurti klase "Zmogus, kuri vaizduoja zmogaus savybes: vardas, amzius        """
# class Zmogus:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius

#     def rodyti_info(self):      #metodas kuris nusako rodyti informacija apie zmogu
#         print(f"Zmogaus vardas yra: {self.vardas}")
#         print(f"Zmogaus amzius yra: {self.amzius}")

# class Darbuotojas(Zmogus):        # sukuriame paveldima klase (inheritance)
#     def __init__(self, vardas, amzius, atlyginimas):   #priskiriame naujas savybes
#         super().__init__(vardas, amzius)            #surasome kokias savybes paveldi
#         self.atlyginimas = atlyginimas       #aprasome papildoma savybe

#     def rodyti_info(self):
#         super().rodyti_info()     #Pnaudija tevines klases metoda, print vardas, amzius
#         print(f"Darbuotojo atlyginimas yra: {self.atlyginimas}")

# zmogus = Zmogus("Antaniukas", 12)     #sukuriame objekta is tevines klases
# darbuotojas = Darbuotojas("Kazys", 52, 1500)  # sukuriame vaikines klases objekta

# zmogus.rodyti_info() 
# print()   # padeda tarpa vaizdavime
# darbuotojas.rodyti_info()



"""   sukurti produkto krepselio funkcionaluma. turint prdoukta ir krepseli"""

# class Product:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price

#     def display_info(self):
#         print(f"Produkto pavadinimas yra: {self.title}")
#         print(f"Produkto kaina yra: {self.price} €")

# class DiscountedProduct(Product):
#     def __init__(self, title, price, discount_percentage):
#         super().__init__(title, price)
#         self.discount_percentage = discount_percentage

#     def calculate_discounted_price(self):
#         discount_amount = self.price * (self.discount_percentage / 100)
#         discount_price = self.price - discount_amount
#         return discount_price
    
#     def display_info(self):
#         super().display_info()
#         print(f"Discount {self.discount_percentage} %")
#         print(f"Total amount: {self.calculate_discounted_price()} €")

# class ShoppingCart(Product):
#     def __init__(self):
#         super().__init__(title=None, price=None)
#         self.product = []

#     def add_product(self, product):
#         self.product.append(product)
#         print(f"Product {product.title} was added to cart successfully")

#     def remove_product(self, product):
#         if product in self.product:
#             self.product.remove(product)
#             print(f"Product {product.title} was removed from cart successfully")
#         else:
#             print(f"Product {product.title} is not in the cart")

#     def calculate_cart_total_amount(self):
#         total_price = 0
#         for product in self.product:
#             total_price += product.price
#         return total_price
        


# produktas = Product("Pienas", 2.00)
# produktas1 = DiscountedProduct("Vaisiai", 2.99, 10)
# produktas2 = Product("Sviestas", 3.99)

# vezimelis = ShoppingCart()
# vezimelis.add_product(produktas)
# vezimelis.add_product(produktas1)
# vezimelis.add_product(produktas2)
# print()
# for product in vezimelis.product:
#     product.display_info()
#     print()
    
# total_price = vezimelis.calculate_cart_total_amount()
# print(f"Total cart amount: {total_price} €")
# print()

# vezimelis.remove_product(produktas)

# total_price = vezimelis.calculate_cart_total_amount()
# print()
# print(f"Total new cart amount: {total_price} €")
# print()
