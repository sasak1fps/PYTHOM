salario =float(input('digite seu salario : '))
desconto = 15/100 
destot= salario  + (desconto * salario)
print('o salario antigo era de {:.2f}  , com  {:.2f}%  , de aumento o novo salario é {:.2f}'.format(salario , desconto , destot) )