personagem = {
    "nome": "Link",
    "Classe": "Mago",
    "nivel": 1,
    "inventario": []
}

item1 = input("Digite o nome do primeiro item: ")
item2 = input("Digite o nome do segundo item: ")

personagem["inventario"].append(item1)
personagem["inventario"].append(item2)

print("\nPersonagem:")
print(personagem["nome"])
print(personagem["Classe"])
print(personagem["nivel"])

print("\nInventário:")
for item in personagem["inventario"]:
    print("-", item)
