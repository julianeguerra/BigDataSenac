total_multas = []
multa = 4
peso_permitido = 100
def calcular_multa(peso_total):
    if peso_total == 0:
        print('Você não pescou nada. Encerrando o programa…')
    elif peso_total > peso_permitido:
        peso_excedente = peso_total - peso_permitido
        print(f'O valor da multa é: {peso_excedente * 4:.2f} reais')
        total_multas.append(peso_excedente)
    
    elif peso_total < peso_permitido or peso_total == 100:
        print('Peso dentro do limite. Nenhuma multa a pagar')

        
while True:
    try:
        peso_peixes = float(input('Quantos quilos você pescou hoje? '))
        calcular_multa(peso_peixes)
        if peso_peixes == 0:
            break
    except ValueError:
        print('ERRO: insira um número válido.')

print('**** Multas registradas: ****')


for multa in total_multas:
    print(f'R$ {multa:.2f}')
print(f'Total de multas: R$ {sum(total_multas)}.')


    
