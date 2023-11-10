num = list()
n = 0
while True:
    n= (int(input('digite um numero  ')))
    if n not in num:
        num.append(n)
    else:
        print('valor duplicado:   ')
    r =str(input('quer continuar [S/N] '))
    if r in "nN":
        break
print(f'{num}')