# ex. 02
#  Enquanto verdade, inserir o valor do produto
# executar comandos de calculo
# se, valor == 0, interromper

while True:

    valor = float(input("insira o valor de seu produto: "))
    if (valor == 0):
        break
    desconto = valor * (0.6)
    nvvalor= valor-desconto

    print(f"preço: R$ {valor:.2f} | desconto: R$ {desconto:.2f} | preço c/ desconto: R$ {nvvalor:.2f}")
