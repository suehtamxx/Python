pessoas = {
    'elder': 20,
    'matheus': 17,
    'maia': 20,
    'oliveira': 15
}
pessoas_maior = {}
print(pessoas)

for i in pessoas:
    if pessoas[i] >= 18:
        pessoas_maior[i] = pessoas[i]

print(pessoas_maior)    
