num=[ [] , [] ]
valor = 0
for c in range(1,8):
    valor = int(input(f'digt {c} valor    '))
    if valor %2==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'pares:      {num[0]}')
print(f'impares:    {num[1]}')