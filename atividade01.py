nota1= float(input('Qual a sua nota no 1º trimestre?'))

nota2= float(input('Qual a sua nota no 2º trimestre?'))

nota3= float(input('Qual a sua nota no 3º trimestre?'))

nota4= float(input('Qual a sua nota no 4º trimestre?'))

calculo_nota = (nota1 + nota2 + nota3 + nota4) / 4

media = print(f'A sua média é {calculo_nota}.')

if calculo_nota >= 7:
    print(f'Aprovado!')

elif calculo_nota >= 5:
        print(f'Em recuperação!')

else:
      print(f'Reprovado!')

    
















