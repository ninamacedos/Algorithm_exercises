# ex.: 12 'verificação de uma senha válida'

def password(senha):
    maiuscula = 0
    minuscula = 0
    numero = 0
    for i in senha:
        if (i.isupper()):
            maiuscula += 1
        if (i.islower()):
            minuscula += 1
        if (str.isnumeric(i)):
            numero += 1

    if (minuscula < 1 or maiuscula < 1 or numero < 1 or len(senha) < 8):
        return False

    return True

def main():
    senha = input("Crie uma senha de no mínimo 8 caracteres, com ao menos uma letra maiuscula, minuscula e um número(espaços serão ignorados): ")
    senha = senha.strip()
    senha = senha.replace(" ", "")

    if password(senha) == False:
        print("senha inválida")
    else:
        print("senha válida")
if __name__ == "__main__":
    main()   