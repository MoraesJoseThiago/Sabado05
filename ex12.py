numeros = []
contador = 0

while contador < 5:
    n = int(input("Digite um numero: "))
    numeros.append(n) #coloca o número no final da lista
    contador += 1

print("Maior:", max(numeros))
print("Menor:", min(numeros))
