#ex.: 02 "inteiros em ordem decrescente"

list = []
while True:
    num_int = int(input("Insira um número na lista (0 para parar): "))
    if num_int != 0:
        list.append(num_int)
    else:
        break

print("lista em ordem decrescente: ")
list.sort()
lista_decresc= list[::-1]
for num_int in lista_decresc:
    print(num_int)
