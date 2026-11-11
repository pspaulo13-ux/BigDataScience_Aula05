numero - float(input('Digite um número: '))

match numero:
    case 0:
        print('O número é zero.')

    case n if n > 0:
        print('O número é positivo')    

    case _:
        print('O número é negativo')

