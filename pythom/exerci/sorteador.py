import random 
n1 = input('digite um nome :')
n2 = input('digite um nome :')
n3 = input('digite um nome :')
n4 = input('digite um nome :')
list = [n1 ,n2 , n3,n4]
print('o nome sorteado foi {} !!' .format(random.choice(list)))