#ex.: 06 "lista de divisores"

def div_inteiro(lista, num):
    n = 0
    lista = []
    while (n < num):
        n += 1
        if (num%n == 0 and num != n):
            lista.append(n)
    print(f"Os divisores de {num} são: {lista}")

def main():
    lista = []
    num = int(input("Insira um número: "))
    div_inteiro(lista, num)
if __name__ == "__main__":
    main()


