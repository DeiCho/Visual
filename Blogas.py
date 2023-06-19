# class Blog:
#     def __init__(self):
#         self.posts = []
    
#     def create_post(self, title, description):
#         post = {
#             "blog_title": title,
#             "blog_description": description
#          }
#         self.posts.append(post)
#         print("Irasas buvo sekmingai sukurtas")

#     def display_all_posts(self):
#         if not self.posts:
#             print("No blogs posts found")
#         else:
#             print("Blog posts: ")
#             for post in self.posts:
#                 print(f"Title: {post['blog_title']}")
#                 print(f"Description: {post['blog_description']}")
#                 print("--------------")
#     #keiciam bendra turini
#     def update_post(self, title, updated_description):
#         for post in self.posts:
#             if post["blog_title"] == title:
#                post["blog_description"] = updated_description
#                print("Blog's post was updated")
#                break
#         else:
#             print("Blog's post was not found")

#     def delete_post(self, title):
#         for post in self.posts:
#             if post["blog_title"] == title:
#                 self.posts.remove(post)
#                 print("Post was removed successfully")
#         else:
#             print("Post was not found")
                    

# post1 = Blog() #naudojam ta pati objekta, ness jis neturi atributu
# post1.create_post("Duomenu analitikos studentai uzkariavo pasauli", "Gyveno karta duomenu analitikai, kurie panoro ismokti programuoti")
# post1.create_post("Mokslininkai isrado nauja metoda", "Kaip greiciau ismokti duommenu analitikos")
# post1.create_post("Kulinarijos sedevrai", "Tukstantis ir vienas receptas")

# post1.update_post("Duomenu analitikos studentai uzkariavo pasauli", "Gyveno karta duomenu analitikai, kurie panoro ismokti programuoti ir uzkariauti interneta")
# post1.delete_post("Duomenu analitikos studentai uzkariavo pasauli")
# post1.display_all_posts()

# # CRUD create, read, update, delete


"""----------------------------------ZODYNAS--------------------------------"""
# zmogus = {
#     "vardas": "Jonas",
#     "amzius": 27,
#     "miestas": "Vilnius"
# }
# print("Mano vardas: ", zmogus['vardas'])


# zmogus["lytis"] = "Vyras"
# #pridedame nauja elementa i savo zodyna
# print("As esu ", zmogus["lytis"])

# # keiciame reiksmes

# zmogus["amzius"] = 20

# print("Atsiprasau man yra: " zmogus['amzius'], "metu")

#triname reiksmes

# del zmogus["miestas"]

# print(zmogus['miestas'])

# iteruojame per visus zodyno elementus

# for key, value in zmogus.items():
    # print(key, ":", value)

#Tuple - kortele

# kordinates = (10,50)
# print(kordinates[1])

# kordinates1 = (54, 42, 12)

# sujungtos_kordinates = kordinates + kordinates1
# print(sujungtos_kordinates)