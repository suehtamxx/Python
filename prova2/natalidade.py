def calcular_anos(x,y):
    anos = 0
    while x < y:
        x *= 1.03
        y *= 1.015
        anos += 1
    return anos

x = float(input())
y = float(input())
print(calcular_anos(x,y))