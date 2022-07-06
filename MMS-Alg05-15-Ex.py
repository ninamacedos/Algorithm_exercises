#ex.: 15 'Dígitos hexadeciamis e decimais"

def hex2int(num_hexa):

    if int(num_hexa) < 10:
        print(f"{num_hexa} para decimal é {num_hexa}")
    elif num_hexa == "A":
        print(f'{num_hexa} em hexadecimal para decimal é 10')
    elif num_hexa == "B":
        print(f'{num_hexa} em hexadecimal para decimal é 11')
    elif num_hexa == "C":
        print(f'{num_hexa} em hexadecimal para decimal é 12')
    elif num_hexa == "D":
        print(f'{num_hexa} em hexadecimal para decimal é 13')
    elif num_hexa == "E":
        print(f'{num_hexa} em hexadecimal para decimal é 14')
    elif num_hexa == "F":
        print(f'{num_hexa} em hexadecimal para decimal é 15')
    else:
        print("Por favor, escolha um valor de 0 a F")
def int2hex(int_num):
    if int_num < 10:
        print(f"{int_num} para decimal é {int_num}")
    elif int_num == 10:
        print(f"{int_num} em hexadecimal é 'A'")
    elif int_num == 11:
        print(f"{int_num} em hexadecimal é 'B'")
    elif int_num == 12:
        print(f"{int_num} em hexadecimal é 'C'")
    elif int_num == 13:
        print(f"{int_num} em hexadecimal é 'D'")
    elif int_num == 14:
        print(f"{int_num} em hexadecimal é 'E'")
    elif int_num == 15:
        print(f"{int_num} em hexadecimal é 'F'")
    else:
        print("Por favor, escolha um valor de 0 a 15")

def main():
    num_hexa = input("Digite um número em hexadecimal [0-F] para convertê-lo em decimal: ")
    hex2int(num_hexa)
    int_num = int(input("Digite um número decimal [0-15] para convertê-lo em hexadecimal: "))
    int2hex(int_num)

if __name__ == "__main__":
    main()