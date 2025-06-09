import random

# Get two numbers from the user and covert them to integers
a = int(input("Enter the lower bound: "))
b = int(input("Enter the upper bound: "))

# Pick a random int using randint
random_num = random.randint(a, b)
print(f"The Universe has chosen a random number between your answers. Here is you angel numer: {random_num}")
