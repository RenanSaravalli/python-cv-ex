#Crie uma tupla preenchida com os 20 primeiros colocados do Campeonato brasileiro de futebol, na ordem de colocação. Depois mostre: A) Apenas os 5 primeiros colocados. B) Os últimos 4 colocados da tabela C) Uma lista com os times em ordem alfabética D) Em que posição na tabela está o time do Bahia
br = ('Palmeiras','Grêmio','Atlético-MG','Flamengo','Botafogo','Bragantino','Fluminense','Athletico-PR','Internacional','Fortaleza','São Paulo','Cuiabá','Corinthians','Cruzeiro','Vasco da Gama','Bahia','Santos','Goiás','Coritiba','América-MG')
print('-='*10)
print(f'Lista de times do Brasileirão: {br}')
print('-='*10)
print(f'Os 5 primeiros são {br[:5]}')
print('-='*10)
print(f'Os 4 últimos são {br[16:20]}')
print('-='*10)
print(f'Times em ordem alfabética : {sorted(br)}')
print('-='*10)
print(f'O Bahia está na {br.index("Bahia")+1}ª posição')