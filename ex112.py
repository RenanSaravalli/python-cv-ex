#Dentro do pacote utilidadescev que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como função input(), mas com uma validação de dados para aceitar apenas valores monetários.
from ex111.utilidadescev import dado
from ex112.utilidadescev import moeda

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22 )