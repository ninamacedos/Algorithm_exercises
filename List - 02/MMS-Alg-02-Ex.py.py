#lista 2

#1
d= int(input("informe o nº de dias = "))
h= int(input("informe a qntd. de horas = "))
minut= int(input("informe a qntd. de minutos = "))
seg= int(input("informe a qntd. de segundos = "))
seg_total= (d*24*60**2) + (h*60**2)+(minut*60)+seg
print("Total de segundos do intervalo de tempo =", seg_total )

#2
seg= int(input("Insira o nº de segundos que deseja converter:"))

dias= seg // (24*(60**2))
seg_restantes= seg % (24*(60**2))
horas= seg_restantes // (60**2)
seg_restantes= seg_restantes % (60**2)
minutos= seg_restantes // 60
seg_restantes= seg_restantes % 60

print("%d:%.2d:%.2d:%.2d" % (dias, horas, minutos, seg_restantes))

#3
from datetime import datetime
data_e_hora = datetime.now()
print("Data e hora atuais =" , data_e_hora)

#4
a= int(input("Insira um numero inteiro a = "))
b= int(input("Insira um numero inteiro b = "))
c= int(input("Insira um numero inteiro c = "))
d= (a+b+c)-((min(a,b,c))+(max(a,b,c)))
print(min(a,b,c))
print(d)
print(max(a,b,c))

#5
valorpago= int(input("Informe o valor a ser pago em centavos"))
valorrecebido= int(input("informe o valor recebido em centavos"))
troco= valorrecebido-valorpago

cinq_cents= int(troco/50)
troco= troco-cinq_cents*50
vint_cents= int(troco/25)
troco= troco-vint_cents*25
dez_cents= int(troco/10)
troco= troco-dez_cents*10
cinco_cents= int(troco/5)
um_cent= troco- cinco_cents*5

print("troco a ser pago:")
print("um centavo: ", um_cent)
print("cinco centavos: ", cinco_cents)
print("dez centavos: ", dez_cents)
print("vinte e cinco centavos: ", vint_cents)
print("cinquenta centavos: ", cinq_cents)

#6
inteiro= int(input("insira um numero inteiro com 4 algarismos"))
mili= inteiro//1000
inteiro= inteiro-(mili*1000)
cent= inteiro//100
inteiro= inteiro-(cent*100)
dez= inteiro//10
unid= inteiro-(dez*10)
print("soma dos 4 algarismos = ", mili+cent+dez+unid)


#7
i= int(input("insira um numero inteiro com 3 algarismos"))
c= i//100
i= i-(c*100)
d= i//10
u= i-(d*10)
print("centena = ", c*100)
print("dezena = ", d*10)
print(" unidade = ", u)

#8
inter= int(input("insira um nº de 3 algarismos: "))
cento= inter//100
inter= inter-(cento*100)
dezn= inter//10
unidade= inter-(dezn*10)
print("nº inverso = ", unidade,dezn,cento )
   #***********ou usando st:*********
st = (input("insira um nº de 3 algarismos: "))
reversed(st)
print(' número invertido'.join( reversed(st) ))

#9
data= int(input("Insira uma data inteira, no formato DDMMAA: "))
dia_dz= data// 10**5
data= data-(dia_dz*(10**5))
dia_un= data// 10**4
data= data-(dia_un*(10**4))

mes_dz= data// 10**3
data= data-(mes_dz*(10**3))
mes_un= data// 10**2
data= data-(mes_un*(10**2))

ano_dz= data//10
data= data-(ano_dz*10)
ano_un= data
datainversa= (ano_dz*10**5)+(ano_un*10**4)+(mes_dz*10**3)+(mes_un*10**2)+(dia_dz*10)+(dia_un)
print("data invertida: ", datainversa)

#10
num_matricula= int(input("Insira o número de matricula no formato AASDDD: "))
a_dez= num_matricula//10**5
rest_matricula= num_matricula - (a_dez*(10**5))
a_un= rest_matricula//10**4
rest_matricula= rest_matricula- (a_un*(10**4))
ano= (a_dez*10)+a_un
semest= rest_matricula// 1000
print("ano da matricula: ", ano , "semestre do aluno: ", semest)



