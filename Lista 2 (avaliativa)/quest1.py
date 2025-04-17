def tamString(s):
    cont = 0
    for i in s:
        cont += 1
    return cont

s = input('Digite uma string:\n')
print(f'essa string contem {tamString(s)} caracteres')