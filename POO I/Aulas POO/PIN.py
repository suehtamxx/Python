x = 0

while x <= 40:
    if ((x % 4 == 0 or x % 10 == 0) and x != 40):
        print('PIN')
    elif x == 40:
        print('FIM')
    else:
        print(x)
    x += 1