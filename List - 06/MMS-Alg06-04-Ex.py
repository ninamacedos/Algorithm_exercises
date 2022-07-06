#ex.: 04 'Evitando duplicatas'

palavras = []
   
while True:
    palavra = input("Digite uma palavra (vazio para sair): ")
    if (palavra == " "):
        break
    if (not(palavra in palavras)):
        palavras.append(palavra)

for palavra in palavras:
    print(palavra)




