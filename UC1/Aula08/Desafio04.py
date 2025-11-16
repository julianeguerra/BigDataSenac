'''
Regras do ano bissexto: É divisível por 4, exceto para anos divisíveis por 100, a
menos que sejam também divisíveis por 400. (Ex: 2000 e 2400 são bissextos; 1900
e 2100 não são)
'''

def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

try:
    ano_usuario = int(input('Insira um ano:'))
    ano = eh_bissexto(ano_usuario)
    
    if ano: # Se 'resultado' for True
        print(f"O ano {ano_usuario} É bissexto.")
    else: # Se 'resultado' for False
        print(f"O ano {ano_usuario} NÃO é bissexto.")
except ValueError:
    print('ERRO: insira um ano váldido.')      
    
