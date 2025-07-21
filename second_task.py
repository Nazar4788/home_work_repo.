import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max or quantity > (max-min + 1):
        return[]
    result = random.sample(range(min,max + 1), quantity)

    return sorted(result)

print(get_numbers_ticket(1, 49, 6))


          