def fatorial(n):
	fat = 1
	while n > 0:
		fat *= n
		n -= 1
	return fat

fat = fatorial(4)
#print(fat)
def expo(x,e):
	return x**e
exponencial = expo(2,2)


def potencia(x,n):
	cos = 1
	e = 1
	sinal = 1
	for i in range(1, n):
		cos += sinal * expo(x,e)/fatorial(e)
		e+=1
	cos = cos**x
	return cos
cos = potencia(5,4)
print(cos)
