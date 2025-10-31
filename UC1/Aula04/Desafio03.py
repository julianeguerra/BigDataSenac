preco_combustivel = 6.15
odometro_inicial = float(input('Insira a km inicial: '))
odometro_final = float(input('Insira a km final: '))
litros_gastos = float(input('Quantos litros de combustível foram gastos?'))
valor_recebido = float(input('Total recebido.'))

distancia = odometro_final - odometro_inicial

consumo = distancia / litros_gastos

custo = litros_gastos * preco_combustivel

lucro = valor_recebido - custo

print(f'Consumo é {consumo} e lucro é {lucro}.')