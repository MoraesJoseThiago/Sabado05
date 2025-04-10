#20- Peça ao usuário para digitar nomes e idades, armazene num dicionário e depois mostre as pessoas maiores de idade.

pessoas = {}

quantidade = int(input("Quantas pessoas você vai cadastrar? "))

for i in range(quantidade):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    pessoas[nome] = idade

#??
