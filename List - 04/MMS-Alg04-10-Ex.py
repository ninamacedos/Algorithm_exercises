#ex.: 10 "palíndromo"

palavra = input("Informe a palavra: ")
tamanho = len(palavra)
a = 0

while a < tamanho:
    if (palavra[a] != palavra[tamanho - a - 1]):
        print("Não é um palíndromo")
        break
    a += 1
else:
    print("É um palíndromo")