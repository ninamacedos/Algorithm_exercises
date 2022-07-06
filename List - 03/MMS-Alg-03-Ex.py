#lista 3
from math import sqrt

#1
number= int(input("insira um número"))
rest= number % 2
if(rest == 0):
    print("par")
else:
    print("impar")

print("********************************************************************************************")

#2
idade_canina= int(input("insira a idade de seu cachorro: "))
if (idade_canina > 2):
    idade_humana= (idade_canina-2) *4+2*10.5
    print("Anos em idade humana = ", idade_humana)
elif (idade_canina < 0):
    print("idade não aceita")
else:
    idade_humana= idade_canina* 10.5
    print("Anos em idade humana", idade_humana)

print("********************************************************************************************")

#3
letra= input("insira uma letra qualquer: ")
letra= letra.upper()
if (letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):  
    print(letra, "é uma vogal!" )
else:
    print("é uma consoante!")

print("********************************************************************************************")

#4
poligono= int(input("Insira a quantidade de lados de um polígono regular e descubra seu nome = "))
if (poligono < 3 or poligono > 10):
    print("erro: quantidade de lados invalidas")
else:
    if (poligono ==3):
        print("triângulo")
    elif (poligono == 4):
        print("quadrilátero")
    elif (poligono == 5):
        print("pentágono")
    elif (poligono == 6):
        print("hexágono")
    elif (poligono == 7):
        print("heptágono")
    elif (poligono == 8):
        print("octágono")
    elif (poligono == 9):
        print("eneágono")
    elif (poligono == 10):
        print("decágono")

print("********************************************************************************************")

#5
mes= input("insira um mês e descubra sua quantidade de dias : ")
if (mes == "janeiro"):
    print(mes,"contém 31 dias")
elif (mes == "fevreiro"):
    print(mes,"contém 28 ou 29 dias")
elif (mes == "março"):
    print(mes,"contém 31 dias")
elif (mes == "abril"):
    print(mes,"contém 30 dias")
elif (mes == "maio"):
    print(mes,"contém 31 dias")
elif (mes == "junho"):
    print(mes,"contém 30 dias")
elif (mes == "julho"):
    print(mes,"contém 31 dias")
elif (mes == "agosto"):
    print(mes,"contém 31 dias")
elif (mes == "setembro"):
    print(mes,"contém 30 dias")
elif (mes == "outubro"):
    print(mes,"contém 31 dias")
elif (mes == "novembro"):
    print(mes,"contém 30 dias")
elif (mes == "dezembro"):
    print(mes,"contém 31 dias")

print("********************************************************************************************")

#6
lado_1= int(input("insira o comprimento do primeiro lado de um triâgulo: "))
lado_2= int(input("insira o comprimento do segundo lado de um triâgulo: "))
lado_3= int(input("insira o comprimento do segundo lado de um triâgulo: "))

if (lado_1==lado_2==lado_3):
    print("esté é um triângulo do tipo equilátero")
elif (lado_1==lado_2 or lado_1==lado_3 or lado_2==lado_3):
    print("este é  um triângulo do tipo isóceles")
else:
    print("este é um triângulo do tipo escaleno")

print("********************************************************************************************")

#7
db= int(input("insira o nivél de decibeis e identifique o/os tipo(s) de barulho: "))
if (db== 40 ):
    print(" tipo de barulho: sala silenciosa")
elif (db== 70 ):
    print(" tipo de barulho: despertador")
elif (db== 106 ):
    print(" tipo de barulho: cortador de grama")
elif (db== 130 ):
    print(" tipo de barulho: britadeira")
elif (db > 106 and db <130 ):
    print(" o nivel do barulho está entre: britadeira e cortador de grama")
elif (70<db<106):
    print("o nivel do barulho está entre: cortador de grama e despertador")
elif (40<db<70):
    print("o nivel do barulho entre: sala silenciosa e despertador")
else:
    (db < 40 or db > 130)
    print("o valor inserido não corresponde ao intervalo entre [40,130], isira um valor contino no intervalo")

print("********************************************************************************************")

#8
nota= input("insira uma nota musical (A,B,C,D,E,F OU G), conforme o sistema da escola anglo-saxônica: ")
x= int(input("insira a casa em que se encontra a nota, podendo variar de [0,8]: "))

if (nota.upper()== "A"):
    hz= 440.00 / (2**(4-x))
    print (nota.upper(),hz ,"Hz")
elif (nota.upper()== "B"):
    hz= 493.88 / (2**(4-x))
    print (nota.upper(),hz ,"Hz")
elif (nota.upper()== "G"):
    hz= 392.00 / (2**(4-x))
    print (nota.upper(),hz ,"Hz")
elif (nota.upper()== "F"):
    hz= 349.23 / (2**(4-x))
    print (nota.upper(),hz ,"Hz")
elif (nota.upper()== "E"):
    hz= 329.63 / (2**(4-x))
    print (nota.upper(),hz ,"Hz")
elif (nota.upper()== "D"):
    hz= 293.66 / (2**(4-x))
    print (nota.upper(),hz ,"Hz")
elif (nota.upper()== "C"):
    hz= 261.63 / (2**(4-x))
    print (nota.upper(),hz ,"Hz")

print("********************************************************************************************")

#9
dia= int(input("insira um dia [1-31]: "))
mes= input("insira um mês: ")

if (dia== 1 and mes== "janeiro"):
    print("essa data corresponde à confraternização universal")
elif (dia==21 and mes=="abril"):
    print("está data corresponde ao feriado de Tiradentes")
elif (dia== 1 and mes== "maio"):
    print("está data corresponde ao feriado do Dia do Trabalho")
elif (dia== 7 and mes== "setembro"):
    print("está data corresponde ao feriado da Independência do Brasil")
elif (dia==12 and mes== "outubro"):
    print("está data corresponde ao feriado de Nossa Senhora Aparecida")
elif (dia==2 and mes=="novembro"):
        print("está data corresponde ao feriado de Finados")
elif (dia==15 and mes=="novembro"):
    print("está data corresponde ao feriado da Proclamação da República")
elif(dia==25 and mes=="dezembro"):
    print("está data corresponde ao feriado de Natal")
else:
    print(dia,mes, "não corresponde a nenhum feriado nacinoal")

print("********************************************************************************************")

#10
c= input("insira a letra correspondente à coluna: ")
l= int(input("insira o número correspondente à linha: "))
rest= (l % 2)

if(rest==0 and (c== "a" or c=="c" or c=="e" or c=="g")):
    print("a cor correspondete à: ", (c,l) ,"é branca")

elif(rest!=0 and (c=="b" or c=="d" or c=="f" or c=="h")):
    print("a cor correspondete à: ", (c,l) ,"é branca")

else:
    print("a cor correspondete à: ", (c,l) ,"é preta")

print("********************************************************************************************")

##11
import math
a= int(input("insira o valor de a: "))
b= int(input("insira o valor de b: "))
c= int(input("insira o valor de c: "))
discriminante= ((b**2) - (4*a*c))

if(a==0):
    print("não é uma função quadrática, pois a==0")
    
elif(discriminante < 0):
    print("a equação não possui raizes reais")

elif(discriminante == 0):
    raiz= ((-b + discriminante) / (2*a))
    print("só existe uma raiz real", raiz)

else:
    (discriminante > 0)
    raiz1= ((-b + math.sqrt(discriminante))/(2*a))
    raiz2= ((-b - math.sqrt(discriminante))/(2*a))
    print("a equação possui duas raizes reais, ", raiz1 , raiz2)

print("********************************************************************************************")

#12
ano= int(input("insira um ano: "))
if(ano%400 == 0):
    print(ano, "é bissexto")
elif(ano%100 == 0):
    print(ano, "não é bissexto")
elif(ano%4 == 0):
    print(ano, "é bissexto")
else:
    print(ano, "não é bissexto")

