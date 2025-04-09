import random

letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"

senha = ""
for i in range(10):  # Gera uma senha de 10 caracteres
    senha += random.choice(letras) #choise escolhe aleatoriamente um item de uma sequência

print("Sua nova senha", senha)
