media = []
n = 0
while n != -1:
    n = float(input('digite um valor:\n'))
    if n != -1:
        media.append(n)
    m = len(media)
print(f'{sum(media)/m:.2f}')    