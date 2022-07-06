#ex.: 05 "Negativos, zeros e positivos"

negativos = []
zeros = []
positivos = []

while True:
    inteiros = input("Insira inteiros negativos e positivos (enter para sair): ")
    if (inteiros == ""):
        break
    
    inteiros = int(inteiros)
    if (inteiros < 0):
        negativos.append(inteiros)
    elif (inteiros == 0):
        zeros.append(inteiros)
    else:
        positivos.append(inteiros)

print("")
print("negativos, zeros e positivos, respectivamente, em lista: ")
print("")
for inteiros in negativos:
    print(inteiros)
for inteiros in zeros:
    print(inteiros)
for inteiros in positivos:
    print(inteiros)