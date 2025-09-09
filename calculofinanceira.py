saldo_devedor = 60000
meses = 120
amortizacao = 500
juros = 0.01112133
prestacao = 0
total = 0

for i in range(1, meses + 1):
    prestacao = amortizacao + (saldo_devedor * juros)
    total += prestacao
    saldo_devedor -= amortizacao
total += 40000
print(f'{total:.2f}')

