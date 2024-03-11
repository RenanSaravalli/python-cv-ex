#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples o sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from ex115.arquivo import *
from ex115 import menu
from time import sleep

arq = 'pessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu.menu(['Mostrar pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])

    if resp == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)

    elif resp == 2:
        menu.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = menu.leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resp == 3:
        menu.cabeçalho('Saindo do programa... Até logo'.center(42))
        break

    else:
        menu.cabeçalho('ERRO! digite uma opção válida!')
    sleep(1)