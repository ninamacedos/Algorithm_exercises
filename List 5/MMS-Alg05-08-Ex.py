#ex.: 08 "Letras maiúsculas (reconhecer .  ? !)"

def correcao(frase):
    frase = frase.lower()
    frase = frase.strip()
    res = ""
    maiusc = False
    for i in range(0, len(frase)):
        try:
            if (frase[i - 1] == "." or frase[i - 1] == "!" or frase[i - 1] == "?" or i == 0):
                res += frase[i].upper()
                if (frase[i] == " "):
                    maiusc = True                
            else:
                if (maiusc):
                    res += frase[i].upper()
                    maiusc = False
                else:
                    res += frase[i]
        except IndexError:
            res += frase[i]
    return res

def main():
    frase = input("Digite uma frase: ")
    print("\n" * 130)
    print("frase corrigida:", correcao(frase))

if __name__ == "__main__":
    main()
            

