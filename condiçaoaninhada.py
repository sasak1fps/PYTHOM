nome = str(input('qual é seu nome ? : '))
if  nome == 'gustavo':
    print('que nome bonito !')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print(' \033[1;33;45m{} \033[m seu nome é bem popular no Brasil'.format(nome))
elif nome in 'ana claudia jessica juliana':
    print('belo nome  feminino')
else:
    print('seu nome é bem normal. ')
print('tenha um bom dia \033[1;32;43m {} \033[m'.format(nome))
