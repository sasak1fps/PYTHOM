import datetime
atual = datetime.date.today().year
count = 0
cont=0
for c in range(0 ,7,1):
    nasc= int(input('digite o ano de nascmineto  '))
    idade = atual - nasc
    if idade >= 21:
        count+=1
        print('\033[1;32messa pessoa é maior')
    elif idade <21:
        cont+=1
        print('\033[1;31m essa pessoa é menor ')
print('temos \033[1;32m{} maiores de idade '.format(count))
print('temos \033[1;31m{} menores de idade '.format(cont))