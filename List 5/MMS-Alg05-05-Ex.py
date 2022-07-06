#ex.: "números ordinais"

n = int(input("Insira um número entre o intervalo [1,2]: "))
num = n
def num_ordinal(num):
    if num == 1:
        return 'primeiro(a)'
    elif num == 2:
        return 'segundo(a)'
    elif num == 3:
        return 'terceiro(a)'
    elif num == 4:
        return 'quarto(a)'
    elif num == 5:
        return 'quinto(a)'
    elif num == 6:
        return 'sexto(a)'
    elif num == 7:
        return 'sétimo(a)'
    elif num == 8:
        return 'oitavo(a)'
    elif num == 9:
        return 'nono(a)'
    elif num == 10:
        return 'décimo(a)'
    elif num == 11:
        return 'décimo(a) primeiro(a)' 
    elif num == 12:
        return 'décimo(a) segundo(a)'

def main():
    if num > 0 and num < 12:
        print (F'O ordinal de {n} é {num_ordinal(num)}')
    else:
        print("")
if __name__ == "__main__": 
    main()