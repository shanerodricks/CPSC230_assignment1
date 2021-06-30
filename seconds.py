import random

random.randint(1,86400)

second = random.random()
minutes = second//60
hours = minutes//60

print("time: " + hours + minutes + seconds)
