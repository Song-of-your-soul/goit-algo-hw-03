import random


def get_numbers_ticket(min, max, quantity=1): # 3 параметри: мінімаоьне число, максимальне, кількість чисел в списку
    lottery_numbers = []
    number = ""
    try:
        if min > 0 and max <= 1000:
            while len(lottery_numbers) < quantity:  
                number = random.randint(min, max)
                if number not in lottery_numbers:
                    lottery_numbers.append(number) # Поки кількість елементів менше ніж задана, нові елементи будуть додаватись
                else:
                    continue
        else:
            return lottery_numbers # Якщо мінімум менший за 0, чи максимум більший за 1000, то поверне пустий список
        lottery_numbers.sort()
        return lottery_numbers
    except ValueError:
        print("Please enter correct data")           
