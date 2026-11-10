valor_pedido = float(input("Digite o valor: "))
distancia = float(input('Qual a distancia? '))
frete = 8
if valor_pedido > 50 and distancia <= 3:
    valor_final = valor_pedido
    print('Frete Gratis!')

else:
    valor_final = valor_pedido + 8

    print(f'Frete de R$ {frete} adicionado ao pedido')
    print(f"Valor final: R$ {valor_final:.2f}")
    


