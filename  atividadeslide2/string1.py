frase = input('Digite uma frase:\n')
op = 0
while op != 6:
    op = int(input('1 - Original\n2 - Maiusculas\n3 - Minusculas\n4 - Primeira letra cada palavra em maiusculo\n5 - Nova frase\n6 - Sair\n'))
    if op == 1:
        print(frase)
    elif op == 2:
        frasem = frase.upper()
        print(frasem)
    elif op == 3:
        frasem = frase.lower()
        print(frasem)
    elif op == 4:
        frasel = frase.title()
        print(frasel)
    elif op == 5:
        frase = input('Digite uma nova frase:\n')
    elif op == 6:
        print('Tchau...')