frase = input("Digite a frase: ").lower()
vogais = "aeiou"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print("Total de vogal", contador)
