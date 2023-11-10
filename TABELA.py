times = ('Corinthians','Palmeiras','Santos','Gremio','Cruzeiro','Flamengo','Vasco', 'Chapecoense','Atletico', 'Botafogo','Atletico-Pr','Bahia','Sao paulo', 'Fluminense' ,'Sporte Recife' , 'EC vitoria' , 'Curitiba' , 'Avai','Ponte preta' , 'Atletico-go')
for t in times:
    print(t)
print(f'os 5 primeiros sao {times[0:5]}')
print(f'os 5 ultimos sao {times[-5:]}')
print(f' times em ordem : {sorted(times) }')
print(f'o chapecoense esta na {times.index('Chapecoense')+1}ª posicao')