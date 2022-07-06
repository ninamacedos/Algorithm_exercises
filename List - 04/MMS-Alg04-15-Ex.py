#ex.: 15 "decimal ---> binario"

result = ""
q = int(input("Insira um decimal: "))
while q != 0:
    r = q%2
    r = str(r)
    result = r + result
    q = q//2

print("O seu número em binário é: ", result)