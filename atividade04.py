print('''
[1] - Sul
[2] - Norte
[3] - Leste
[4] - Oeste
[5/6] - Nordeste
[7 a 9] - Sudeste
[10] - Centro-Oeste
[11] - Noroeste


''')
opcao = int(input('Qual o codigo de origem? '))

match opcao:
    case 1:
        print('Sul')
    case 2:
        print('Norte') 
    case 3:
        print('Leste')
    case 4:
        print('Oeste')
    case 5|6:
        print('Nordeste')
    case codigo if 7<= opcao <= 9:
        print('Sudeste')
    case 10:
        print('Centro-Oeste')
    case 11:
        print('Noroeste')
    case _:
        print('Importado.')