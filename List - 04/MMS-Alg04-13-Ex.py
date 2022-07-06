#ex.: 13 "fatoração numerica, n <= 2"

n = int(input("Insira um inteiro n <= 2: "))
f = 2
while f <= n:
    if (n%f) == 0:
        n = n/f
        print(f)
    else:
        f += 1