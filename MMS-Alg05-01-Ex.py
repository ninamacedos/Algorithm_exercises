#ex.: 01 "hipotenusa"
# Função para calcular o valor da hip (teorema de pitágoras)

import math

b = float(input("Informe o valor do cateto b: "))
c = float(input("Informe o valor do cateto c: "))

def pitag(b,c): 
    a = math.sqrt(b**2 + c**2)
    return a

print (" Hipotenusa = " , pitag(b,c))