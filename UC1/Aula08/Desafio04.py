def eh_bissexto(ano):
    if (ano % 4 == 0) or (ano % 400 == 0) not (ano % 100 == 0):
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} não é bissexto.')

try:
    ano = int(input('Insira um ano:'))
except ValueError:
    print('ERRO: insira um ano váldido.')      

eh_bissexto(ano)

'''
Regras do ano bissexto: É divisível por 4, exceto para anos divisíveis por 100, a
menos que sejam também divisíveis por 400. (Ex: 2000 e 2400 são bissextos; 1900
e 2100 não são)
'''