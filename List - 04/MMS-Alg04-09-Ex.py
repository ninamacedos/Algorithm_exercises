#ex.: 09 "raiz quadrada" 

n = int(input("Insira um número: "))
raiz = n/2
i = 0

while raiz*raiz - n < 10**(-12) or n - raiz*raiz < 10**(-12):
    print(raiz)
    raiz = (raiz + (n/raiz))/2
    print(raiz)
    i +=1

    if i == 10:
        break

print("Raíz: %.12f" % raiz)