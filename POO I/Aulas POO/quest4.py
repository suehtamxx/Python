qtd_gasosa = float(input("Digite a quantidade de litros:\n"))
tipo = input('Alcool(A) ou Gasolina(G):\n')
if tipo == 'A' or tipo == 'a':
    valor = qtd_gasosa * 3.45
    if qtd_gasosa <= 20:
        valor -= valor * 0.03
    elif qtd_gasosa > 20:
        valor -= valor * 0.05
elif tipo == 'G' or tipo == 'g':
    valor = qtd_gasosa * 4.53
    if qtd_gasosa <= 20:
        valor -= valor * 0.04
    elif qtd_gasosa > 20:
        valor -= valor * 0.06
print(f'O valor do combustivel {tipo} a ser pago pelo cliente é de: R${valor:.2f}')



