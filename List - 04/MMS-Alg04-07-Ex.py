#ex.: 07 "aproximacao do valor de pi"

n = 3
print(n)
i = 4
cont = 1

while (cont <= 14):
    cont += 1
    teste =  i // 2
    if (teste % 2 == 0):
        n = n + (4/((i - 2) * (i - 1) * (i)))
    else:
        n = n - (4/((i - 2) * (i - 1) * (i)))
    
    i = i + 2
    print(round(n, cont))

