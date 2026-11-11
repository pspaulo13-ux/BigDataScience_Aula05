valor_compra = float(input('Qual o valor da compra ? '))
fidelidade = input('O cliente é cadastrado no programa de fidelidade [Sim/Não] ? ').lower()[0]
frete = 25.00
compra_frete = valor_compra + frete

if valor_compra > 200 or fidelidade == "Sim":
    print(f'Parabéns, Você acaba de ganhar o frete grátis!\n O valor do seu pedido é de R${valor_compra}')

else:
    print(f'Você está não está apto a ganhar o frete grátis, nesse caso será cobrado o valor de R$ {frete}\nResumo da compra:\nValor da compraR${valor_compra}\nValor do frete R${frete}\nValor final R${compra_frete}')

