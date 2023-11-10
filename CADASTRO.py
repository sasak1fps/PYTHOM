tot18= toth=  totf = 0
while True:
    idade= int(input(' idade '))
    sexo= ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F]')).upper().strip()[0]
    if idade >=18:
        tot18+=1
    if sexo == 'M':
        toth+=1
    if sexo == 'F' and idade <20:
        totf+=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'pessoas com mais de 18 anos {tot18} ')
print(f'temo {toth}homems cadastrados')
print(f'temos {totf} mulheres com menos 20')
print('fim')    