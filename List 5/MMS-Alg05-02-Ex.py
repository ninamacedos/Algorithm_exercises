#ex.: 02 "Tárifa de taxi"

fixvalue= float(input("Insira o valor fixo da corrida ou digite 0 p/ valor padrão: "))
if (fixvalue == 0):
    fixvalue = 4

distancefee= float(input("Insira a tarifa por m percorrido ou digite 0 p/ valor padrão: "))
if (distancefee == 0):
    distancefee = 0.25

vari_dist= float(input("Insira a distância padrão da tarifação em metros ou digite 0 p/ valor padrão: "))
if (vari_dist == 0):
    vari_dist = 140

fvari_dist = (vari_dist/1000)               #distância padrão em km

trav_dist= float(input("insira a distância percorrida em km: "))

def calc(trav_dist):
    f_value = ( fixvalue +  ((trav_dist/fvari_dist) * distancefee))
    return f_value

print (f"A tarifa total é de R$ ", calc(trav_dist)) 