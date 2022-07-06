# exercicio 3
# definir o inicio da contagem em "0", para 0 + 10 (multiplos de 10)
# Enquanto verdade, executar comando de conversão
# Se celsius > 100 = interromper o comando de conversão

c= 0
while True:
    fh= (c*9/5) + 32
    print ("celsius: ", c, "  fahrenheit: ", fh)
    c = c + 10
    if (c > 100):
        break
        