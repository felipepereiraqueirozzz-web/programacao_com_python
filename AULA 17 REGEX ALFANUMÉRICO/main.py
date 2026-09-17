import re
codigo = input("Digite um codigo: ")
while re.fullmatch(r"[a-z0-9]{5}", codigo):
    codigo = input("Digite novamente: ")

    
print("Senha aceita")