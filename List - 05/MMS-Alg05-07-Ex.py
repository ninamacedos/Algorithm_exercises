#ex.: "triangulo válido"

l1 = input("Insira o valor do priemiro lado: ")
l2 = input("Insira o valor do segundo lado: ")
l3 = input("Insira o valor do terceiro lado: ")

def main():

    def triang(l1,l2,l3):
        if l1 < l2+l3:
            return 'válido'
        elif l2 < l1+l3:
            return 'válido'
        elif l3 < l2+l3:
            return 'válido'
        else :
            return 'inválido'

    print (f'triangulo {triang(l1,l2,l3)}')


if __name__ == "__main__":
    main()