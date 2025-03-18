valor = 5.0 #inicializo todas as variaveis necessarias
ingresso = 120
lucro_max = 0.0
qtd_ing = 0
valor_ing = 0.0
while valor >= 1.0:
    lucro = (valor * ingresso) - 200 #calculo do lucro
    if lucro_max < lucro: #aqui eu verifico se o resultado é maior do que o lucro_max que ja tem, assim eu consigo pegar o maior lucro
        lucro_max = lucro #e aqui dentro eu faço as atribuicoes do que for necessario
        qtd_ing = ingresso
        valor_ing = valor
    print(f'Preço do ingresso = {valor}, Quantidade = {ingresso}, Lucro = {lucro}') #print de todos os loop's
    valor -= 0.50 #aqui eu decremento de 0.50 em 0.50, de acordo com o que foi pedido
    ingresso += 26 #e aqui incremento os 26 ingressos a cada decremente de 0.50

print(f'Lucro maximo = {lucro_max}\nValor do ingresso = {valor_ing}\nQuantidade de ingressos = {qtd_ing}') #e aqui é o print da parte do lucro maximo
    