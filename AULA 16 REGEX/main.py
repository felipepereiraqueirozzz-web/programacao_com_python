import re
codigo = input("Digite um codigo!")
if re.fullmatch(r"\d{4}",codigo):
   print("Codigo Valido")
else:
    print("Codigo Invalido")