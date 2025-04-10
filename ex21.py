#21- Faça um jogo de adivinhação onde o programa escolhe um número de 1 a 10 e o usuário tenta adivinhar.

import random

aleatorio = random.randint(1, 10)

chute = 0

while aleatorio != chute:
    chute = int(input("Seu palpite (entre 1 a 10): "))

    if chute < aleatorio:
        print("Errou")
    elif chute > aleatorio:
        print("ERROU")
    else:
        print("Parabéns! Você acertou!")
        break
