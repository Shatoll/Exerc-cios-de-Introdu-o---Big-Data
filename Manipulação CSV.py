from socket import SOMAXCONN

arquivo = open("idades.csv", "a")

for i in range(0,100):
    arquivo.write("Louis, "+str(i)+ "\n")

# Concatenação
# nome = "João"
# sobrenome = "Gomes da Silva "
# idade = 19
# idade2 = 78
# soma = str(idade) + str(idade2)
# print(nome + sobrenome + "é um bom aluno" + str(idade) + str(soma))
