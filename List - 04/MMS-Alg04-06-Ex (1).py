#ex.:06 "bits de paridade"

palavra = 0

while palavra != "":
    palavra = input("Digite uma palavra binária com 8 bits: ")

    if len(palavra) !=8:
        print("Erro 1 - Sua palavra não tem 8 bits")
        break
    
    for digito in palavra:
        if digito !="1" and digito != "0":
            print("Erro 2 - Sua palavra não tem só 0s e 1s")
            break
    
    uns = palavra.count("1")
    if uns%2 == 0: #numero par de 1
        print("O bit de paridade é 0")
    else:
        print("O bit de paridade é 1")