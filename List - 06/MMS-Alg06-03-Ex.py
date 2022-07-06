#ex.: 03 "removendo extremos"

def remove_extrem(list,num):
    while True:
        num = int(input("Insira um número na lista: "))
        n = 0
        if num != 0:
            n += 1
            list.append(num)
            list.sort()
        else:
            if len(list) < 4:
                print("Erro - Insira pelo menos 4 valores.")
                list = []
            else:
                list.remove(list[0])
                list.remove(list[n-1])
                print(f"lista sem os extremos: {list}")
                break

def main():
    lista = []
    numero = 1
    remove_extrem(lista, numero)

if __name__ == "__main__":
    main()