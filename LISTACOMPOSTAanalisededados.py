temp = []
princ = []
while True:
    temp.append(str(input('digite um nome   ')))
    temp.append(float(input('peso:          ')))
    princ.append(temp[:])
    temp.clear()
    resp =  str(input('continuar [S/N]'))
    if resp in 'nN':
        break

print(princ)
print(f'ao todo, {len(princ)} cadastrados')
print(f'o maior peso é {max(princ)}')
print(f'o menor peso é {min(princ)}')