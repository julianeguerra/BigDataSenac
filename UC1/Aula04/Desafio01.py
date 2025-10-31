altura = float(input('Insira a altura em metros.'))
largura = float(input('Insira a largura em metros.'))
potencia = float(input('Insira a potência da lâmpada.'))


area = altura * largura

n_lampadas = (area * potencia)/3

print(f'São necessárias {n_lampadas} lâmpadas.')

#a cada 3 m² = 3 lampadas 
#para limitar as casas decimais > :.2f

