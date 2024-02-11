
import re

def normalize_number(phone_number): # Приводить номер телефону до стандарту
    pattern = r"\+?\d+" # Шукає номер із можливо наявним плюсом
    phone_number = ''.join(re.findall(pattern, phone_number)) # Знаходить всі випадки співпадіння патерну та поєднує номер в один елемент
    if len(phone_number) == 12:
        phone_number = "+" + phone_number
    elif len(phone_number) == 10:
        phone_number = "+38" + phone_number
    return phone_number 

def normalize_list(phone_numbers): # Приводить список номерів телефонів до стандарту
    for phone in phone_numbers: # Перевіряє кожний номер у заданому списку
        correct_numbers.append(normalize_number(phone))
    return correct_numbers

correct_numbers = []
    

print(normalize_list(raw_numbers))