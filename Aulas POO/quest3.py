salario_h = float(input('Digite quanto voce ganha por hora:\n'))
horas = int(input('Quantas horas voce trabalhou no mes:\n'))
salario = salario_h * horas
ir = salario * 0.11
inss = salario *0.08
sindicato = salario * 0.05
salario_liquido = (salario - ir - inss - sindicato)
print(f'Salario bruto: R${salario:.3f}\nINSS: R${inss}\nIR: R${ir}\nSindicato: R${sindicato}\nSalario Liquido: R${salario_liquido}')