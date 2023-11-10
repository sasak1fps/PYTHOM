somaidade = 0
media = 0
maioridadehomem = 0 
nomevelho= 0
totmulher= 0
for p in range(1,5):
    print('==={}ºPESSOA==='.format(p))
    nome=str(input('NOME ')).strip().upper()
    idade = int(input('IDADE '))
    sexo = str(input('SEXO [M/F]')).strip()
    somaidade += idade
    if p ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher+=1

media = somaidade / 4
print('a media do grupo é {} anos'.format(media))
print('o homem mais velho tem {} anos  e se chama {} '.format(maioridadehomem,nomevelho))
print(' mulheres menores que {} anos '.format(totmulher))