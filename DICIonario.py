aluno = dict()
aluno ['nome'] = str(input('nome:      '))
aluno ['media']= float(input(f'media de {aluno["nome"]}:    '))
if aluno['media'] >=7:
    aluno['situaçao']='aprovado'
elif 5 <=aluno['media']<7:
    aluno['situaçao'] = 'recuperaçao'
else:
    aluno['situaçao'] = 'reprovado'
    print('                    ')
for k,v in aluno.items():
    print(f'  -{k} e igual a {v}')