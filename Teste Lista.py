### Criar uma lista cadastro de nomes e idades; mostra a soma ou a média de todas as idades:

from wsgiref.util import guess_scheme


nomes = []
idades = []
a = ""
while a != "sair":
    nome = input("Qual é o seu nome? ")
    nomes.append(nome)
    idade = input("Qual é a sua idade? ")
    idades.append(idade)
    a = nome

    # Comando para eliminar os últimos elementos após inserir "sair":
    if a == "sair":
        nomes.pop()
        idades.pop()

# Imprimir nomes inseridos:
# for nome in nomes:
#   print(nome)

# calculando a soma da idade:
soma = 0
for idade in idades:
    soma = int(idade) + int(soma)

print("soma = ", str(soma))

# calculando e imprimindo a média das idades:
print("média = ", str(soma/len(idades)))
print(idades)
idades.sort()
tamanho = len(idades)

print(idades)
print("mediana = ", str(idades[int(tamanho/2)]))

# Imprimir a quantidade de elementos da lista "nomes" e "idades":
print(len(nomes))
print(len(idades))