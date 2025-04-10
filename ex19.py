#19- Crie uma função que receba uma lista e retorne a soma dos elementos.

def somar_lista(lista):
    return sum(lista)

numeros = input("Digite os numeros separados por espaço: ")
lista = list(map(int, numeros.split()))

print("Soma:", somar_lista(lista))
