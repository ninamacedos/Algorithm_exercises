#ex.: 08 "Somente palavras"

def separa_palavra(frase):
    frase.strip()
    palavras= []
    pontuacoes = [ "!", "?", ".", ":", ":",","," "]
    inicio = 0
    for n in range (0, len(frase)):
        if ((frase[n]) in pontuacoes):
            if (frase[n - 1] in pontuacoes):
                inicio += 1
            else:
                palavras.append(frase[inicio:n])
                inicio = n + 1
    return palavras
            
def main():
    frase = input("Informe um texto com acentos: ")
    fraseformatada = separa_palavra(frase)
    print(fraseformatada)
if __name__=="__main__":
    main()