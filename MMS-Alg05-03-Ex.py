#ex.: 03 "calculadora de envio e-commerce"

qntd = int(input("Informe a quantidade itens comprados: "))

def calcfrete(qntd):
    if qntd == 1:
        frete = 10.95
    elif qntd >= 2:
        frete = (((qntd - 1) * 2.95) + 10.95)
    else:
        frete = 0
    return frete

print("o frete é: R$ ", calcfrete(qntd))