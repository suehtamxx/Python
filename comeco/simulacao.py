import numpy as np

# Definir parâmetros de cada time com base nos dados recentes
# Exemplo para dois times: Time A e Time B

# Taxa média de gols por jogo dos últimos 5 jogos
gols_marcados_time_A = 1.83
gols_marcados_time_B = 1.5

# Taxa média de gols sofridos por jogo dos últimos 5 jogos
gols_sofridos_time_A = 1
gols_sofridos_time_B = 1.16

# Número de simulações para cada partida
simulacoes = 10

# Função para simular uma partida
def simular_partida(gols_marcados, gols_sofridos):
    # Média de gols esperados usando uma distribuição de Poisson
    gols_time_1 = np.random.poisson(gols_marcados)
    gols_time_2 = np.random.poisson(gols_sofridos)
    return gols_time_1, gols_time_2

# Armazenar resultados de cada simulação
resultados_A_vs_B = []

for i in range(simulacoes):
    # Simular a partida entre Time A e Time B
    gols_A, gols_B = simular_partida(gols_marcados_time_A, gols_sofridos_time_B)
    resultados_A_vs_B.append((gols_A, gols_B))

# Calcular a média de resultados
media_gols_A = np.mean([resultado[0] for resultado in resultados_A_vs_B])
media_gols_B = np.mean([resultado[1] for resultado in resultados_A_vs_B])

# Exibir o resultado médio esperado
print(f"Placar médio esperado: Time A {media_gols_A:.1f} x {media_gols_B:.1f} Time B")
