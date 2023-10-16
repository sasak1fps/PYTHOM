from random import shuffle
n1 = input('primeiro aluno  : ')
n2 = input('segundo aluno : ' )
n3 = input('terceiro aluno :  ')
n4= input('quarto aluno :   ')

list = [n1 , n2 , n3 , n4 ]
shuffle(list)
print('a ordem sera :  \n{}  '.format(list))