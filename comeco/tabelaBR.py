import requests
from bs4 import BeautifulSoup
import pandas as pd

# Função para extrair dados de probabilidade de vitória
def extrair_probabilidades(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Localiza a tabela
    tabela = soup.find('table')
    linhas = tabela.find_all('tr')[1:]  # Ignora o cabeçalho

    # Estrutura para armazenar dados
    dados = []

    for linha in linhas:
        colunas = linha.find_all('td')
        
        # Verifica se há colunas suficientes na linha
        if len(colunas) < 8:
            continue  # Ignora a linha se não tiver todas as colunas esperadas
        
        time = colunas[1].text.strip()  # Nome do time
        pvm = float(colunas[2].text.strip())  # Prob. de vitória mandante
        pem = float(colunas[3].text.strip())  # Prob. de empate mandante
        pdm = float(colunas[4].text.strip())  # Prob. de derrota mandante
        pvv = float(colunas[5].text.strip())  # Prob. de vitória visitante
        pev = float(colunas[6].text.strip())  # Prob. de empate visitante
        pdv = float(colunas[7].text.strip())  # Prob. de derrota visitante
        
        dados.append([time, pvm, pem, pdm, pvv, pev, pdv])

    # Cria DataFrame
    df_probabilidades = pd.DataFrame(dados, columns=['Time', 'PVM', 'PEM', 'PDM', 'PVV', 'PEV', 'PDV'])
    
    return df_probabilidades

# Função para extrair dados de gols feitos
def extrair_gols_feitos(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Localiza a tabela
    tabela = soup.find('table')
    linhas = tabela.find_all('tr')[1:]  # Ignora o cabeçalho

    # Estrutura para armazenar dados
    dados = []

    for linha in linhas:
        colunas = linha.find_all('td')
        
        # Verifica se há colunas suficientes na linha
        if len(colunas) < 3:
            continue  # Ignora a linha se não tiver colunas suficientes
        
        time = colunas[1].text.strip()  # Nome do time
        gols_feitos = int(colunas[2].text.strip())  # Gols feitos
        
        dados.append([time, gols_feitos])

    # Cria DataFrame
    df_gols_feitos = pd.DataFrame(dados, columns=['Time', 'Gols Feitos'])
    
    return df_gols_feitos


# Função para extrair dados de gols sofridos
def extrair_gols_sofridos(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Localiza a tabela
    tabela = soup.find('table')
    linhas = tabela.find_all('tr')[1:]  # Ignora o cabeçalho

    # Estrutura para armazenar dados
    dados = []

    for linha in linhas:
        colunas = linha.find_all('td')
        
        # Verifica se há colunas suficientes na linha
        if len(colunas) < 3:
            continue  # Ignora a linha se não tiver colunas suficientes
        
        time = colunas[1].text.strip()  # Nome do time
        gols_sofridos = int(colunas[2].text.strip())  # Coluna dos gols sofridos
        
        dados.append([time, gols_sofridos])

    # Cria DataFrame
    df_gols_sofridos = pd.DataFrame(dados, columns=['Time', 'Gols Sofridos'])
    
    return df_gols_sofridos
# URLs das tabelas
url_probabilidades = "https://www.mat.ufmg.br/futebol/tabela-de-probabilidades_seriea/"
url_gols_feitos = "https://www.mat.ufmg.br/futebol/melhor-ataque_seriea/"
url_gols_sofridos = "https://www.mat.ufmg.br/futebol/melhor-defesa_seriea/"

# Coletando dados de cada uma das tabelas
df_probabilidades = extrair_probabilidades(url_probabilidades)
df_gols_feitos = extrair_gols_feitos(url_gols_feitos)
df_gols_sofridos = extrair_gols_sofridos(url_gols_sofridos)

# Mesclando todos os dados em um único DataFrame para fácil análise
df_completo = df_probabilidades.merge(df_gols_feitos, on="Time").merge(df_gols_sofridos, on="Time")
print(df_completo)

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Função para extrair dados dos jogos restantes
def extrair_jogos_restantes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jogos = []

    # Modifique esta parte de acordo com a estrutura da página de jogos restantes
    tabela_jogos = soup.find_all('table')  # Assumindo que os jogos estão numa tabela
    for row in tabela_jogos[0].find_all('tr')[1:]:
        colunas = row.find_all('td')
        mandante = colunas[0].text.strip()
        visitante = colunas[1].text.strip()
        jogos.append((mandante, visitante))

    return jogos

# URL dos jogos restantes
url_jogos_restantes = "https://www.google.com/search?q=proximos+jogos+brasileirao+2024&sca_esv=85b561e56a3fcf31&rlz=1C1PNQB_enBR1109BR1109&sxsrf=ADLYWIK9KRgwiqlzP0FCh8x93EG6gI1GGw%3A1731353238988&ei=lloyZ7fOO--35OUP0NnKuA4&oq=proximos+jogos+brasi&gs_lp=Egxnd3Mtd2l6LXNlcnAiFHByb3hpbW9zIGpvZ29zIGJyYXNpKgIIATIQEAAYgAQYsQMYgwEYRhj9ATILEAAYgAQYsQMYgwEyBRAAGIAEMgUQABiABDIFEAAYgAQyCxAAGIAEGLEDGIMBMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIcEAAYgAQYsQMYgwEYRhj9ARiXBRiMBRjdBNgBAUjSMlAAWOgqcAF4AZABAJgBngGgAc4WqgEEMC4yMLgBA8gBAPgBAZgCFqAC_x2oAhLCAgcQIxgnGOoCwgIHEC4YJxjqAsICFhAuGIAEGEMYtAIYyAMYigUY6gLYAQHCAgQQIxgnwgIKECMYgAQYJxiKBcICDRAuGIAEGLEDGEMYigXCAgoQABiABBhDGIoFwgIOEAAYgAQYsQMYgwEYigXCAgUQLhiABMICEBAAGIAEGLEDGEMYgwEYigXCAg0QABiABBixAxgUGIcCwgIKEAAYgAQYFBiHAsICDRAAGIAEGLEDGEMYigXCAggQABiABBixA5gDB7oGBggBEAEYCJIHCDEuMjAuNi0xoAeJlgE&sclient=gws-wiz-serp#sie=lg;/g/11vb7cvd3q;2;/m/0fnk7q;mt;fp;1;;;"
jogos_restantes = extrair_jogos_restantes(url_jogos_restantes)

# Função para calcular probabilidade de vitória ajustada por gols
def calcular_probabilidade(jogo, df_probabilidades, df_gols_feitos, df_gols_sofridos):
    mandante, visitante = jogo

    # Probabilidades do mandante
    prob_mandante_vitoria = df_probabilidades.loc[mandante, 'PVM']
    prob_mandante_empate = df_probabilidades.loc[mandante, 'PEM']
    prob_mandante_derrota = df_probabilidades.loc[mandante, 'PDM']
    gols_feitos_mandante = df_gols_feitos.loc[mandante, 'gols_feitos']
    gols_sofridos_mandante = df_gols_sofridos.loc[mandante, 'gols_sofridos']

    # Probabilidades do visitante
    prob_visitante_vitoria = df_probabilidades.loc[visitante, 'PVV']
    prob_visitante_empate = df_probabilidades.loc[visitante, 'PEV']
    prob_visitante_derrota = df_probabilidades.loc[visitante, 'PDV']
    gols_feitos_visitante = df_gols_feitos.loc[visitante, 'gols_feitos']
    gols_sofridos_visitante = df_gols_sofridos.loc[visitante, 'gols_sofridos']

    # Ajuste das probabilidades com base nos gols feitos e sofridos
    fator_ajuste_mandante = gols_feitos_mandante / (gols_feitos_mandante + gols_sofridos_visitante)
    fator_ajuste_visitante = gols_feitos_visitante / (gols_feitos_visitante + gols_sofridos_mandante)

    # Probabilidades ajustadas
    prob_vitoria_mandante = prob_mandante_vitoria * fator_ajuste_mandante
    prob_vitoria_visitante = prob_visitante_vitoria * fator_ajuste_visitante
    prob_empate = (prob_mandante_empate + prob_visitante_empate) / 2

    # Normalizar para que a soma seja 100%
    soma_prob = prob_vitoria_mandante + prob_empate + prob_vitoria_visitante
    prob_vitoria_mandante /= soma_prob
    prob_empate /= soma_prob
    prob_vitoria_visitante /= soma_prob

    return {
        'mandante': mandante,
        'visitante': visitante,
        'prob_vitoria_mandante': prob_vitoria_mandante,
        'prob_empate': prob_empate,
        'prob_vitoria_visitante': prob_vitoria_visitante
    }

# Exemplo de uso
resultados_jogos = []
for jogo in jogos_restantes:
    resultado = calcular_probabilidade(jogo, df_probabilidades, df_gols_feitos, df_gols_sofridos)
    resultados_jogos.append(resultado)

# Exibir resultados
for resultado in resultados_jogos:
    print(f"{resultado['mandante']} vs {resultado['visitante']}:")
    print(f"  Vitória Mandante: {resultado['prob_vitoria_mandante']:.2%}")
    print(f"  Empate: {resultado['prob_empate']:.2%}")
    print(f"  Vitória Visitante: {resultado['prob_vitoria_visitante']:.2%}")
