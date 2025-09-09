import numpy as np
import matplotlib.pyplot as plt

# Dados para o gráfico
meses = [20, 40, 60, 80, 100, 120]

# Custo Total Acumulado (Entrada + Financiamento)
total_custo_price = [60089.4, 80178.8, 100268.2, 120357.6, 140447.0, 160536.4]
total_custo_sac = [62284.0, 82353.4, 100194.4, 115811.2, 129202.5, 140370.4]

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(meses, total_custo_price, marker='o', linestyle='-', label='Sistema Price')
plt.plot(meses, total_custo_sac, marker='o', linestyle='-', label='Sistema SAC')

# Configurar o gráfico
plt.title('Custo Total Acumulado do Financiamento (SAC vs. Price)', fontsize=14)
plt.xlabel('Meses')
plt.ylabel('Custo Total Acumulado (R$)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Salvar o gráfico
plt.savefig('custo_total_acumulado.png')

plt.show()
plt.show()