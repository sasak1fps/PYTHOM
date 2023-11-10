valores= [] 
pares = [] 
impares = []
while True:
    valores.append(int(input('dgt um nmr :                ')))
    resp = str(input('quer continuar  [S/N]  '))
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2==0: 
        pares.append(v)
    elif v %2==1:
        impares.append(v)

print(f'{valores}')
print(f'par:    {pares}')
print(f'impar:  {impares}')