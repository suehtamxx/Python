senha = 0
senha = input('Digite a senha(8 caracteres e pelo menos 1 letra e 1 numero):\n')
while len(senha) < 8 or senha.isalpha() or senha.isdigit():
    if len(senha) < 8:
        print('A senha deve ter 8 caracteres')
    elif senha.isalpha():
        print('A senha deve conter pelo menos um numero:')
    elif senha.isdigit():
        print('A senha deve conter pelo menos uma letra:')
    senha = input('Digite a senha:\n')
for i in senha:
    print(i)