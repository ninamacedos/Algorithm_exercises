#ex.: 01 "inteiros em ordem crescente"

list = []
while True:
    num_int = int(input("Insira um número na lista (0 para parar): "))
    if num_int != 0:
        list.append(num_int)
    else:
        break

print("lista em ordem crescente: ")
list.sort()
for num_int in list:
    print(num_int)

