ficha=list()
while True:
    nome =str(input('nome: '))
    nota1=float(input('nota1: '))
    nota2=float(input('nota2: '))
    media = ((nota1 + nota2) / 2)
    ficha.append([nome ,[nota1 , nota2] , media])
    resp  = str(input(' \033[1;33m quer continuar : [S/N] \033[m '))
    if resp in 'nN':
        break
    
print(f'{"no.":<4} {"NOME":<10} {"MEDIA":>8}')
print('\033[1;33m-*\033[m'*26)
for i , a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}' )
while True:
    print('\033[1;33m-*\033[m'*50)
    opc = int(input('mostrar notas de qual aluno:        \033[1;33m(999 to quit)\033[m'))
    if opc == 999:
        print('\033[1;31mfim\033[m')
        break
    if opc <=len(ficha) -1:
        print(f'notas de \033[1;33m {ficha[opc] [0]} \033[m sao \033[1;33m{ficha[opc] [1]}\033[m')