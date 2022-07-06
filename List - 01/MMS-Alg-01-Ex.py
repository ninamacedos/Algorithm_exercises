from cmath import sqrt
import math
import string 
raiz=math.sqrt(9)
print (raiz)

#1
print ("***********************************************")
print ("Marina Macedo Silva")
print("Rua Coruripe, 86 - Água Verde, Blumenau-SC")
print ("************************************************")

#2
name = (input("Whats your name?"))
print ("Hello",name)

#3
largura = (float(input("inira a largura da sala")))
profundidade = (float(input("insira a profundidade da sala")))
area = largura*profundidade
print(f"A área da sala  de {(area)} m²")

#4
larg_ter = (float(input("inira a largura do terreno")))
profund_ter = (float(input("insira a profundidade do terreno")))
area_ter = (larg_ter*profund_ter)
print (f"A área do terreno é de {(area_ter)/10**4} hectares") 

#5
max_1l = (float(input("insira o número de recipientes até 1 1L")))
maior_1l = (float(input ("insira o número de recipientes com mais de 1L")))
print (" o total de créditos retornados é R$ %.2f" % ((max_1l*0.10)+(maior_1l*0.25)))

#6
sc = (float(input("Insira o valor do suco")))
pt_pr = (float(input("Insira o valor do prato principal")))
sobrem = (float(input("Insira o valor da sobremesa")))
print ("O valor total da conta é R$ %.2f" % (((sc+pt_pr+sobrem)*0.10)+(sc+pt_pr+sobrem)))

#7
n= (int(input("Insira úm numero qualquer inteiro e positivo")))
print(f"A soma de todos os números inteiros de 1 a n é {(n)*(n+1)/2}")

#8
bug= int(input("insira aqui a quantidade de bigigangas"))
quinq= int(input("insita aqui a quantidade de quinquilharias "))
total_peso= (bug*75)+(quinq*112)
print(f"o peso total de quinquilharias e bugigangas é,{(total_peso)} gramas.")

#9
api_1= (float(input("Api inicial")))
p1= api_1*1.12
p2= p1*1.12
p3= p2*1.12
print("montante do primeiro periodo R$ %.4f" % p1)
print("montante do segundo periodo R$ %.4f" % p2)
print("montante do terceiro periodo R$ %.4f" % p3)

#10
import math
a=int(input("insira um numero inteiro 'a'"))
b=int(input("insisra um numero inteiro 'b'"))
#operacoes
s=a+b
d=a-b
p=a*b
q=a//b
r=a%b
log= math.log (a,10)
e=a**b
print("soma de a e b",s)
print("diferenca de a-b",d)
print("produto de a e b",p)
print("quociente de a por b",q)
print("resto de a por b,r", r)
print("logaritimo de a na base 10", log )
print("potencia a elevado a b",e)

#11
import math
from turtle import distance

lt_1= float(input("Insira a latitude do ponto 1 em graus"))
lg_1= float(input("Insira a longitude do ponto 1 em graus"))
lt_2= float(input("Insira a latitude do ponto 2 em graus"))
lg_2= float(input("Insira a longitude do ponto 2 em graus"))
lt_1= math.radians(lt_1)
lg_1= math.radians(lg_1)
lt_2= math.radians(lt_2)
lg_2= math.radians(lg_2)
dist= 6371.01* math.acos(math.sin(lt_1)*math.sin(lt_2)+ math.cos(lt_1)*math.cos(lt_2)*math.cos(lg_1-lg_2))
print("A distancia de um ponto a para b em Km: %.2f"% dist)

#12
from math import pi
raio= float(input("inista o raio do circulo"))
ar= pi*(raio**2)
vl=((4/3)*(pi*(raio**3)))
print("a area do circulo é", ar)
print("volume igual a",vl) 

#13
base=float(input("insira a base do triangulo"))
h_altura=float(input("insira a altura do triangulo"))
form= (base*h_altura)/2
print("a area do triangulo é", form)

#14
from math import sqrt
x1= float(input("insira o prim. lado"))
x2= float(input("insira o seg. "))
x3= float(input("insira o terc. lado "))
y= ((x1+x2+x3)/2)
ar= sqrt(((y-x1)*(y-x2)*(y-x3)*y))
print("a area do triangulo é",ar)

#15
import math
compr= float(input("insira o comprimento de um lado do poligono"))
lados= float(input("insira o numero de lados do poligono"))
ar = ((compr)*lados**2)/(4*math.tan(math.pi/lados))
print("area do poligono e",ar)
