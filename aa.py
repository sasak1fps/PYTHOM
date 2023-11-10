nome =str(input('digite seu nome : ')).strip().upper()
print('a letra a aparece {} vezes'.format(nome.count('A')))
print('a letra a aparece pela privemira vez {}'.format(nome.find('A')+1))
print('aletra a aparece pela ultima vez {} '.format(nome.rfind('A')+1))