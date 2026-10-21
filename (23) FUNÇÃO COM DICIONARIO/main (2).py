personagens = []

def criar_personagem():
    nome  = input("Digite o nome do seu personagem: ")
    classe =  input("Digite  a classe do seu personagem: ")
    nivel = int(input("Digite o nivel do seu personagem: "))
    
    personagem = {
        "nome": nome,
        "classe": classe,
        "nivel": nivel,
    }
    personagens.append(personagem)
    
    print("PERSONAGEM CRIADO")
    print("Nome: ", personagem["nome"])
    print("Classe: ", personagem["classe"])
    print("Nivel: ", personagem["nivel"])
 
 
quantidade = int(input("Quantos personagens deseja criar"))
for i in range(quantidade):
    print("Criando personagem {i +1}")