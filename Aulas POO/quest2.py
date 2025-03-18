peso = float(input('Digite o peso dos peixes:\n'))
if peso >= 51:
    excesso = peso - 50
    multa = excesso * 4
print(f'O excesso é de {excesso:.2f} kg\nA multa é R${multa:.2f}')

             