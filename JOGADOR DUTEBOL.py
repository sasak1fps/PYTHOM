jogador = dict()
partidas = list()
jogador ['nome'] = str(input('nome do jogador:  '))
tot=int(input(f'quantas partidas {jogador["nome"]}jogou?  '))
for c in range(0,tot):
    partidas.append(int(input(f' quantos gols na partidas {c} ')))
jogador['gols'] = partidas[:]
    