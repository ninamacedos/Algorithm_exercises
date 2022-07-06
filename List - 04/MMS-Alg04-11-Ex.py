#ex.: 11 "palíndromo com mais de uma palavra (frases), 
# levando em consideracao remocao de pontos e acentos"

import string
frase = input("Insira a frase: ").upper()
frase = frase.replace(" ", "")

#remocao
i = 0     
punctuation = string.punctuation
while i < len(punctuation):
    frase = frase.replace(punctuation[i], "")
    i += 1

comprimento = len(frase)

i = 0
while i < comprimento:
    if (frase[i] != frase[comprimento - i - 1]):
        print("A frase não é um palíndromo")
        break
    i += 1
else:
    print("A frase é um palíndromo")