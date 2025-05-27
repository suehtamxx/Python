def recursao_degraus(n):
    if n == 0 or n == 1:
        return 1
    return recursao_degraus(n - 1) + recursao_degraus(n - 2)
total = recursao_degraus(5)
print(total)