largura = float(input('Insira a largura em metros.'))
comprimento = float(input('Insira o comprimento em metros.'))
potencia = float(input('Insira a potência da lâmpada.'))


area = largura * comprimento

potencia_necessaria = area * 3

n_lampadas = potencia_necessaria/potencia

n_bocais = area / 3

print(f'São necessárias {n_lampadas}')

#a cada 3 m² = 3 lampadas 
#para limitar as casas decimais > :.2f

