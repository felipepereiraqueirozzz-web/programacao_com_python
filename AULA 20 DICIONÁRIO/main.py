personagens = [
    {"nome": "Bob esponja", "idade": 23},
    {"nome": "Thanos", "idade": 1000}
]
# print(personagens[0]["nome"])
# print(personagens[1]["nome"])
for personagem in personagens:
    print("nome", personagem["nome"])
    print("idade", personagem["idade"])