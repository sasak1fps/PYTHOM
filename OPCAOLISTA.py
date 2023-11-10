valores = list()
while True:
     valores.append(int(input('dgt um nmr :  ')))
     r = str(input('qur continuar ?   [S/N]         '))
     if r in 'nN':
          break
     if 5 in valores:
          print('o numero 5 esta na lista')
     else:
          print('o numero 5 nao esta na lista')
     
valores.sort(reverse=True)
print(f'{valores.sort(reverse=True)}')
print(f'a lista possui {len(valores)} elementos ')