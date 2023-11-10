salario = int(input('digite  o salario do funcionario '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('\033[0;33;44m quem ganhava {:.2f}  passa a ganhar {:.2f}  agora '.format(salario , novo))