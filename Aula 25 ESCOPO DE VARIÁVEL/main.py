# def cadastrar_usuario(nome, idade, cidade="Não informado"):
#    print(f"Cadastro: {nome}, {idade}, {cidade}"")
    
#    cadastrar_usuario(idade = 30, cidade = "SJS", nome = "Carlos")

def mostrar_nome():
    nome = "Joao" # Variavel local
    return nome
#   print(nome) Não funciona
print(mostrar_nome())

numero = 10 #variavel global
def calculo():
    global numero # indica que quero usar a variavel global
    numero = 20 #CRIA uma nova variavel local
calculo()
print(numero)
