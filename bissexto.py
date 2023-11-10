from datetime import date
ano = int(input('digite o ano q deseja  analisar : '))
if ano == 0:
    ano = date.today().year
if  ano % 4 == 0   and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO '.format(ano))
else:
    print('o ano {} nao é BISSEXTO '.format(ano))








