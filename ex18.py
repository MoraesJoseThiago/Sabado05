#18- Escreva uma função que retorne se um número é primo.
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))

if eh_primo(numero):
    print("É primo.")
else:
    print("Não é primo.")
