rank = ('Palmeiras','Flamengo','Cruzeiro','Bragantino','Fluminense','Ceará','Bahia','Corinthians',
       'Mirassol','Atlético-MG','Botafogo','São Paulo','Vasco','Fortaleza','Internacional',
       'Vitória','Grêmio','Juventude','Santos','Sport')
print(f'Lista de times do Brasileirão: {rank}')
print(f'Os 5 primeiros são: {rank[:5]}')
print(f'Os 4 últimos são: {rank[-4:]}')
print(f'Times em ordem alfabética: {sorted(rank)}')
print(f'O Grêmio está na {rank.index('Grêmio')+1}ª posição')