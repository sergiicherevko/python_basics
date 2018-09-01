import random

health = 50

difficulty = 1

potion_health = int(random.randint(25,50))

health  = health + potion_health / difficulty

print(health)
