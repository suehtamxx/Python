produtos = {
    'arroz': 2.50,
    'feijao': 3.50,
    'cebola': 1.50,
    'macarrao': 4.00
}
print(produtos)
nome = input('Digite o nome do produto:\n')
if nome in produtos:
    novo_valor = float(input('Digite o novo valor desse produtos:\n'))
    produtos[nome] = novo_valor
print(produtos)
