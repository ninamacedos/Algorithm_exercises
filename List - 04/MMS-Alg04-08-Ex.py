#ex.: 08

frase = input("Escreva uma frase: ")

for let in frase:
    frase_unicode = ord(let)
    print("Frase em unicode: ",frase_unicode, end = " ")