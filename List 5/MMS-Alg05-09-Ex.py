#ex.: 09 "A string representa um inteiro?"

def isInteger(tex):
    tex = tex.strip()
    for x in range(0, len(tex)):
        if (x == 0):
            if (tex[x] == "+" or tex[x] == "-"):
                continue
        try:
            int(tex[x])
        except ValueError:
            return False
    return True

def main():
    tex = input("Insira um texto: ")
    if (isInteger(tex)):
        print(" True = é inteiro")
    else:
        print("False = não é um inteiro")

if __name__ == "__main__":
    main()