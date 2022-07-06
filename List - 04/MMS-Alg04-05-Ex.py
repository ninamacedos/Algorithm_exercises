#ex. 05
#definir ingresso = 0;
#estabelecer laço, com diferentes limites (condições)

ingresso = 0
while True:
    idade = str(input("Insira as idades, ao final digite enter para parar:"))
    if (idade == ""):
        break
    idade = int(idade)
    if (idade <= 2):
        continue
    elif ( 3 <= idade <= 12):
        ingresso = ingresso + 14
    elif (idade >= 65):
        ingresso = ingresso + 18
    else:
        ingresso = ingresso + 23
print (f"O valor a pagar é de R$: {ingresso:.2f}")


    