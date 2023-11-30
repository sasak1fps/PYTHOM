
c = ('\033[m',
     '\033[0;31;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[0;30;46m'
    )


def ajuda(com):
    titulo(f'acessando  o manual do comando \' {com}\'  ' , c[0])
    print(c[1], end='')

    help(com)
    print(c[2], end='')


def titulo (msg,cor=0):
    tam = len(msg)
    print(c[3] , end='')
    print('~'*tam)
    print(msg)
    print('~'*tam)
    print(c[4] , end='')
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP' , c[5])
    comando = str(input('funcaou ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO' , c[6])