#ex.: 11 "senha aleatória"
import random

def password(comp_pass, carac_pass):
    i = 0
    for i in range(0, comp_pass):
        carac_pass += chr(random.randint(33, 126))       
        i +=1
    return carac_pass


def main ():
    comp_pass = random.randint(7, 10)
    comp_pass = int(comp_pass)
    carac_pass = ""
    carac_pass = str(carac_pass)
    print(f"A senha contém {comp_pass} dígitos")
    print(password(comp_pass,carac_pass))
main()