#ex.: 14 'Datas mágicas'

def magic_dt(d, m, y):
    temp = str(y)

    if (y >= 10):       
        temp = temp[len(temp) - 2] + temp[len(temp) - 1]    
    else:
        temp = temp[len(temp) - 1]

    ano = int(temp)
    if ((d * m) == y):
        return True
    else:
        return False

def d_mes(y, m):
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        return 31
    else:
        if ((y % 400 == 0 or y % 4 == 0) and m == 2):
            return 29
        if (m == 2):
            return 28
        return 30

def main():
    for y in range(1900, 2000):
        for m in range(1, 13):
            for d in range(1, d_mes(y, m) + 1):
                if (magic_dt(d, m, y)):
                    print("%d/%d/%d" % (d, m, y))

if __name__ == "__main__":
    main()
