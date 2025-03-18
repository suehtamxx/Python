import pandas as pd
import requests
import jupyter
requisicao = requests.get("https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2024_-_S%C3%A9rie_A")

tabelas = pd.read_html(requisicao.text)

for tabela in tabelas:
    display(tabela)
