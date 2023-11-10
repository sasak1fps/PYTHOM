from datetime import date
                             #nascimento =int(input('digite o ano de nascimento '))
                      #alistamento = date.today().year - nascimento
                        #print('voce nasceu em {}'.format(nascimento))
                        #print('voce pussi  {} anos'.format(alistamento))
                        #if nascimento ==18:
                        #    print('voce deve se alistar ')
                        #elif nascimento <18:
                        #    print('nao possui idade suficiente para se alistar')
                        #elif nascimento >18:
                        #    print('voce deveria ter se alistado antes')

atual =date.today().year
nasc = int(input('digt ano de mascimentoo :  '))
idade = atual -  nasc
print('quem nasceu {} tem {} anos  em {} '.format(nasc, idade,atual))
if idade == 18:
    print('voce deve se alistar imediatamente ')
elif idade <18:
    saldo = 18 - idade
    print(' ainda faltam {} anos para     o alistamento '.format(saldo))
    ano = atual + saldo
    print('voce ira se alistar em {}'.format(ano))
elif idade >18:
    saldo =  idade - 18
    print('voce ja deveria ter se alistado há {} anos '.format(saldo))
    ano = atual - saldo
    print('voce dever ia  se alistar em {}'.format(ano))