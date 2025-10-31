comprimento = float(input('Comprimento?'))
largura = float(input('Largura?'))
altura = float(input('Altura?'))

cxazul = 1.5

area = 2 * (comprimento + largura) * altura

caixas = area / cxazul

print(f'São necessárias {caixas} caixas.')