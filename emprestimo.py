casa = float(input('digite o valor da casa :\033[32m  \033[m'))
salario = float(input('digite o seu salario \033[32m \033[m'))
anos = int(input('em quantos anos ira paga  '))
prestaçao= casa / (anos * 12 )
minimo = salario * (30/100)
print('para pagar a casa de R$\033[32m{} em\033[m {} anos'.format(casa, anos))
print('a prestaçao sera  de R$\033[32m {}\033[m  '.format(prestaçao)) 
if prestaçao <= minimo:
 print('\033[32m concedido \033[m')
else:
    print('\033[31m negado\033[m ' )