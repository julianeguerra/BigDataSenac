n1 = float(input('Insira a nota 1: '))
n2 = float(input('Insira a nota 2: '))
n3 = float(input('Insira a nota 3: '))
n4 = float(input('Insira a nota 4: '))

media = (n1 + n2 + n3 + n4) / 4

if media > 7:
    print('Aprovado')
elif media >= 5 and media <= 7: # outra opção de escrita: elif 5 <= media <= 7
    print('Recuperação')
else:
    print('Reprovação')