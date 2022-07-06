#ex.: 09 "Abaixo e acima da média"

num_list = []
while True:
    num = input("Informe um número (vazio para sair): ")
    if (num == ""):
        break
    try:
        num_list.append(float(num))
    except:
        print("ERRO")
    
total = 0
for num in num_list:
    total += num
media = total / len(num_list)
print("media:", media)

abaixo_media = False
for num in num_list:
    if (num < media):
        if (abaixo_media == False):      
            print("números menores que a média:")
            abaixo_media = True
        print(num)

if (media in num_list):        
    print("números guais à média: ")
    for num in num_list:
        if (num == media):
            print(num)

acima_media = False
for num in num_list:
    if (num > media):
        if (acima_media == False):
            print("números maiores que a média")
            acima_media = True
        print(num)










