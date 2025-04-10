#Simule um caixa eletrônico: peça um valor e informe quantas notas de 100, 50, 20, 10 e 1 são necessárias.

valor = int(input("Digite o valor para saque: "))

while valor > 1:
    if valor >= 100:
        print("100:", 1)
        valor = valor - 100

    elif valor >= 50:
        print("50:", 1)
        valor = valor - 50

    elif valor >= 20:
        print("20:", 1)
        valor = valor - 20

    elif valor >= 10:
        print("10:", 1)
        valor = valor - 10

    else:
        print("1:", 1)
        valor = valor - 1
