from datetime import datetime
dados= dict()
dados ['nome'] = str(input('nome: '))
nasc = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('carteira de trabalho (0 nao tem ):  '))
if dados['ctps'] != 0:
    dados['contratacao'] =  int(input('ano de contrataçao:  '))
    dados['salario']  = float(input('salario: R$'))
    dados ['aposentadoria'] = dados['idade'] + ((dados['contratacao'] +35)- datetime.now().year)
print('-=*50')
for k , v in dados.items():
    print(f' - {k} tem o valor {v}')