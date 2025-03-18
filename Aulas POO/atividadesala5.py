a = int(input('Digite quantas linhas deseja:\n'))
for i in range(a):
    for j in range(a):
        print('*', end='')
    a-=1
    print('')