#ex.: 14 "binário para decinal, entrada como string, processando digito a digito"

binario = input("Insira um numero binário: ")

c = len(binario)
dec = 0

i = 0
while (i < c):
    dec += int(binario[i]) * (2 ** (c - i -1))
    i += 1

print(dec)