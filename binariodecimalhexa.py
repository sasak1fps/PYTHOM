num = int(input('digite um  numero inteiro:  '))
print(''' escolha uma das  bases para  conversao: 
[ 1] converter para binario
[ 2] converter  para octal 
[ 3] converter  para  hexadecimal      ''')
opçao = int(input('sua opçao: '))
if opçao == 1:
    print(' \033[4;32m{}\033[m covertido para binario é igual a \033[4;32m{}\033[m  '.format(num , bin( num )))
elif opçao == 2:
    print(' \033[4;32m{}\033[m convertido para octal é igual a \033[4;32m{}\033[m '.format(num , oct( num )))
else:
    print(' \033[4;32m{}\033[m convertido para hexadecimal é igual \033[4;32m{}\033[m '.format(num , hex( num )))