a = int(input('Insira um número inteiro: '))
b = int(input('Insira outro número inteiro: '))
c = int(input('Insira mais um número inteiro: '))


primeiro = None
segundo = None
terceiro = None

if a < b and a < c:
    primeiro =  a
    if b < c:
        segundo = b
        terceiro = c
    else:
        segundo = c
        terceiro = b
elif b < a and b < c:
    primeiro = b
    if a < c:
        segundo = a
        terceiro = c
    else:
        segundo = c
        terceiro = a
elif c < a and c < b:
    primeiro =  c
    if a < b:
        segundo = a
        terceiro = b
    else:
        segundo = b
        terceiro = a
else:
    print('Erro nos números inseridos. Tente novamente.')

print(f'Ordem: {primeiro}, {segundo}, {terceiro}')