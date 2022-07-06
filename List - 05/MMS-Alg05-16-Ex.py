#16 'Conversão arbitrária de base numérica'

import time

def hex2int(hex):        #hex para int
    hex = hex.upper()
    comprimento = len(hex)
    total = 0

    i = 0
    while (i < comprimento):
        if (hex[i] == "A"):
            numero = 10
        elif (hex[i] == "B"):
            numero = 11
        elif (hex[i] == "C"):
            numero = 12
        elif (hex[i] == "D"):
            numero = 13
        elif (hex[i] == "E"):
            numero = 14
        elif (hex[i] == "F"):
            numero = 15
        else:
            numero = int(hex[i])

        total += numero * (16 ** (comprimento - i -1))
        i += 1
    
    return total

def int2hex(inteiro):       #int para hex
    saida = ""
    while True:
        resto = inteiro % 16
        inteiro = inteiro // 16
        if (resto == 10):
            saida = "A" + saida
        elif (resto == 11):
            saida = "B" + saida
        elif (resto == 12):
            saida = "C" + saida
        elif (resto == 13):
            saida = "D" + saida
        elif (resto == 14):
            saida = "E" + saida
        elif (resto == 15):
            saida = "F" + saida
        else:
            saida = str(resto) + saida
        if (inteiro < 16):
            if (inteiro == 10):
                saida = "A" + saida
            elif (inteiro == 11):
                saida = "B" + saida
            elif (inteiro == 12):
                saida = "C" + saida
            elif (inteiro == 13):
                saida = "D" + saida
            elif (inteiro == 14):
                saida = "E" + saida
            elif (inteiro == 15):
                saida = "F" + saida
            else:
                saida = str(inteiro) + saida
            break
    return saida

def mensagemErro():                                            
    print("valor inválido")
    time.sleep(1.5)
    print("\n" * 130)

def coletarInt(texto):                #qualquer inteiro
    while True:
        try:
            numero = int(input(texto))
            break
        except ValueError:
            mensagemErro()
    return numero

def main():
    while True:
        hex = input("Informe um número em hexdecimal: ")
        if (hex == ""):
            mensagemErro()
            continue
        hex = hex.upper()
        valid = True
        i = 0
        while i < len(hex):
            try:
                vect = ["A", "B", "C", "D", "E", "F"]
                if (hex[i] in vect):
                    i += 1
                    continue
                else:
                    int(hex[i])
                    i += 1
            except ValueError:
                valid = False
                break
        if (valid):
            break
        else:
            mensagemErro()
    print("Número em decimal:", hex2int(hex))

    print()
    inteiro = coletarInt("Informe um decimal: ")
    print("Número em hexdecimal:", int2hex(inteiro))

if __name__ == "__main__":
    main()