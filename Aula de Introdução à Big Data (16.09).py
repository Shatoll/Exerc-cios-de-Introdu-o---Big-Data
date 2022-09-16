frase = "A bananeira está plantada no quintal do seu João.\n"
print(frase)

# Troca de elementos (palavra):
frase = frase.replace("bananeira", "videira")
print (frase)

# Troca de elementos (letra):
frase = frase.replace("a", "z")
frase = frase.replace("ã", "z")

# Troca de elementos (letras) específicos. Neste caso, apenas os 4 primeiros "z":
frase = frase.replace("z", "a", 4)
print(frase)

# Testa se a condição é verdadeira ou falsa:
print(frase.startswith("0"))
print(frase.startswith("A"))