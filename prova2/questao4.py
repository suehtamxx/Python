def valor_serie(n):
    sinal = 1
    s = 0
    for i in range(1, n+1):
        s += sinal * (i/i**2)
        sinal *= -1
    return s
print(valor_serie(100))

def valor(n):
    s = 0
    m = 1
    for i in range(1, n+1):
        s += m/i
    return s