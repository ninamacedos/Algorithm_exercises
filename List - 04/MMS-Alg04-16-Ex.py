#ex.: "cara ou coroa: simulando series de sorteios"

import random
# A = cara
# O = Coroa

import random

qntd = 0
sorteios = 0
while (qntd < 10):     
    qntdA = 0
    qntdO = 0
    sorteioLocal = 0
    while True:
        lado = random.randint(1, 2)    
        if (lado == 1):
            print("A", end=" ")
            qntdA += 1
            qntdO = 0
        else:
            print("O", end=" ")           
            qntdA += 1
            qntdO = 0
        sorteioLocal += 1
        if (qntdA == 3 or qntdO == 3):
            print("(%.1d sorteios)" % (sorteioLocal))
            sorteios += sorteioLocal
            break
    qntd += 1

total = sorteios / 10

print("Na média, foram necessários %.1f sorteios." % (total))