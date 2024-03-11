#Calcula o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque: 10% de desconto, À vista no cartão: 5% de desconto, em até 2x no cartão: preço normal, 3x ou mais no cartão: 20% de juros.
produto = int(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão    
[ 4 ] 3x ou mais no cartão''')
pagamento = int(input('Qual a opção: '))

if pagamento == 1:
    print('O valor do produto R${:.2f} à vista com 10%, de desconto será de: R${:.2f}'.format(produto, produto - produto * 10 / 100))
elif pagamento == 2:
    print('O valor do produto R${:.2f} à vista no cartão com 5%, de desconto será de: R${:.2f}'.format(produto, produto - produto * 5 / 100))
elif pagamento == 3:
    print('O preço do produto pagando 2x no cartão será o valor normal de R${:.2f}.'.format(produto))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x no cartão será de: R${:.2f}'.format(parcelas,( produto + produto * 20 / 100)/parcelas))
    print('Sua compra de R${:.2f} vai custar no final com 20%, de juros {:.2f}'.format(produto, produto + produto * 20 / 100))
else:
    print('Escolha entre as opções acima!')