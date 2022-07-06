#ex.: 04 "perímetro de um polígono"

import math
x1 = 0
y1 = 0
x2 = 0
y2 = 0

perimetro = 0
while x1 != "":
    x1 = (input("insira a coordenada X de um ponto (enter para sair): "))
    y1 = (input("insira a coordenada Y de um ponto: "))

    x2 = (input("insira a coordenada X de OUTRO ponto: "))
    y2 = (input("insira a coordenada Y de OUTRO ponto: "))

    if x1 != "":
        dist = math.sqrt((int(y2)-int(y1))**2 + (int(x2) - int(x1))**2)
        perimetro = perimetro + dist
        print(f"O perímetro deste polígono é: {perimetro}")
else:
    print("Fim do programa")