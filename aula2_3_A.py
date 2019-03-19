print ('Calculando o custo total de livros')

preco = input('Insira o preco de cada livro: ')

desconto = input('Insira o desconto (%) dado em cima do valor dos livros: ')

quantidade = input('Insira a quantidade de livros que voce deseja comprar: ')

envio = 3.0 + (quantidade - 1)*0.75

print('A taxa total para envio e ', envio , 'reais')

preco_total = (preco * (1 - desconto) * quantidade) + envio

print('O valor total pago deve ser de: ', "%.2f" % preco_total, 'reais')
