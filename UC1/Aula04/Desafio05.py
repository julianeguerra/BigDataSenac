avaliacao1 = float(input('Insira a nota da avaliação 1:'))
avaliacao2 = float(input('Insira a nota da avaliação 2:'))
optativa = None

media = (avaliacao1 + avaliacao2)/2

if media >= 6:
    print('Aprovado')
elif media < 3:
    float(input('Insira a nota da optativa:'))
