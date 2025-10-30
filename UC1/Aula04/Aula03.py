try:
    diadasemana =  int(input('Qual dia da semana você quer saber?'))
    match diadasemana:
        case 1:
            print('Domingo')
        case 2:
            print('Segunda')
        case 3:
            print('Terça')
        case 4:
            print('Quarta')
        case 5:
            print('Quinta')
        case 6:
            print('Sexta')
        case 7:
            print('Sábado')
        case _:
            print('Número inválido para a pergunta.')
except ValueError:
    print('Informação inválida. Informe um número inteiro.')