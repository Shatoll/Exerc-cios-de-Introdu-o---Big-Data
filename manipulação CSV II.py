# arquivo = open("idades.csv", "r")
lista = []
lista = ["Zona Norte", "Zona Sul", "Zona Leste", "Zona Leste", "Zona Central", "Zona Rural"]
print(lista[4])

# inserir elemento na lista:
lista.append("Serra")

# deleta elemento da lista:
del lista[4]

# Remove elemento através da indentificação do nome:
lista.remove("Zona Rural")

# Resultado: ['Zona Norte', 'Zona Sul', 'Zona Leste', 'Zona Leste', 'Zona Central', 'Zona Rural', 'Serra']
print(lista)