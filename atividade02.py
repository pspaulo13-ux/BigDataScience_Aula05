nota_final = float(input('Qual a nota final? '))
frequencia = int(input('Qual a frequencia? '))
valor_mensalidade = float(input('Qual o valor da mensalidade?'))
bolsa = valor_mensalidade * 0.20
valor_mensalidade2 = valor_mensalidade - bolsa

if nota_final >= 7 and frequencia >= 75:
    print(f'Parabens, você tem direito a um desconto de 20% na sua mensalidade')
    print(f'Valor da mensalidade atual R${valor_mensalidade}\n Valor da bolsa R$ {bolsa}\n Valor da mensalidade com bolsa R${valor_mensalidade2}')

else:
    print(f'Você não atingiu os critérios para ganhar a bolsa.\n O valor da sua mensalidade é de R${valor_mensalidade}')

