paises = {
    'brasil': 'brasilia',
    'frança': 'paris',
    'italia': 'roma',
    'argentina': 'buenos aires',
    'alemanha': 'berlim'
}
pais = input('Digite o nome de um pais:\n')
if pais in paises:
    print(f'a capital deste pais: {pais}, é {paises[pais]}')
else:
    print('nao tem esse pais no dicionario\n')