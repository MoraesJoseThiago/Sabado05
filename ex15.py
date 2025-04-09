#polindromo e basicamente a frase ser a msm coisa invertida (ana)

palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print("Sim")
else:
    print("Não")
