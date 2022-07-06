#ex.: 07 "Números perfeitos"

n = 0
num = int(input("Insira um número: "))
divisores = []
while(n < num):
    n +=1
    if (num%n == 0):
        divisores.append(n)

resultado = 0
for i in range(0,len(divisores)-1):
    resultado += divisores[i]
print(f"Os divisores de {num} são: {divisores}")
if (resultado == num):
    print(f"A soma dos divisores é igual à {num} - É um número perfeito")
if (resultado != num):
    print(f"A soma dos divisores não igual à {num}, esse não é um número perfeito")

