nome=input('Qual é o nome da sua cidade? ')
nome.strip()
print('Essa cidade começa com "Santo"? ')
print(nome[0:6].lower()=='santo ') 

cid = input('digite sua cidade :').strip()
print(cid[0:5].upper()=='SANTO')