# Creat a program that generates a random password for the user with 6 alphanumeric characters.
import random
import string

for i in range(6):
    print(random.choice(string.ascii_letters + string.digits + string.punctuation), end='')