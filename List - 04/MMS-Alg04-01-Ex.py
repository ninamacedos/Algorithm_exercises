#ex.: 01 "media aritmetica"

i = 0
soma= 0
while True:
        numero= int(input("Informe um número: "))
        soma += numero;
        i += 1
        if (numero == 0):
            break
print ("Média = :", soma/(i-1))        






