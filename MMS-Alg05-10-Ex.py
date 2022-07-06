# ex.: 10 "números primos"

def primo(n):
    if n == 2:
        return True
    elif n >= 2:
        for d in range (1, n):
            if n % d != 0:
                return True
    else:
        return False

def main():
    n = int(input("Insira um número: "))
    if primo(n) == True:
        print("O número é primo")
    else:
        print("O número não é primo")

main()






