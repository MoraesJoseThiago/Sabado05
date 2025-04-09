num1 = int(input("Digite o 1 numero: "))
num2 = int(input("Digite o 2 numero: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Divisão por zero não é permitida."

print(f"\nResultados entre {num1} e {num2}:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")