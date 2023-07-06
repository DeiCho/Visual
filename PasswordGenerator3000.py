
# from colorama import init, Fore, Back, Style
# import pandas as pd
# import string
# import random

"""    kuriame Password generator   """

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

