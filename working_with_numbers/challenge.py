# Generate a random integer between 1 and 100, and check if the result is an even number
import random

rand_num = random.randint(1,100)

print(bool(rand_num % 2))