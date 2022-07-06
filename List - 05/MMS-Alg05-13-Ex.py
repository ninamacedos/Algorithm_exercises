# ex.: 13 'Dias de um mês'

def mes(m,y):
    
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        print("31 dias")
    elif (m == 3 or m == 6 or m == 9 or m == 11):
        print("30 dias")
    elif ((y % 400 == 0 or y % 4 == 0) and m == 2):
            print("29 dias")
            if (mes == 2):
                print("28 dias")
           
def main():
    y = int(input("Insira um ano no formato (0000): "))
    m = int(input("Insira um mês (1-12): "))

    while 1 > y > 12 :
        print('Erro, meses de [1-12]: ')
        y = int(input("Insira um ano no formato (0000): "))
        m = int(input("Insira um mês, no intervalo de [1-12]: "))
     
    mes(m,y)
if __name__ == "__main__":
    main()



       