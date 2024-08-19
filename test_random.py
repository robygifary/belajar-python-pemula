import random

users = ["Robby", "Syakir", "Muharik", "Rasya", "Raffa", "Abiw", "Mahesa", "Azka", "Fatan", "Arya", "Habibi"]

down_limit = 0
up_limit = len(users) -1

random_int = random.randint(down_limit, up_limit)

winner = users[random_int]
print(winner)