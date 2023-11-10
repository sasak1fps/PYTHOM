from datetime import date
ano = int(input('digite o ano de nascimento : '))
atual = date.today().year
idade = atual - ano 
if idade <= 9:
    print('atleta mirim')
elif idade >9 and idade <=15:
    print('atleta infaantil')
elif idade >15 and idade<=19:
    print('atleta junior')
elif idade >19 and idade<=25:
    print('atleta senior')
elif idade >25:
    print('atleta mestre')