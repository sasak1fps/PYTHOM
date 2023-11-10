sexo = str(input('DIGA O SEU SEXO [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input(' DADOS INVALIDOS , TENTE NOVAMENTE:  ')).strip().upper()[0]

print('{} valido '.format(sexo))       
