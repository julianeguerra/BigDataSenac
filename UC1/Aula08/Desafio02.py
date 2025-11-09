lista_pessoas = int(input('Quantas pessoas devemos avaliar?'))

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def obter_classificacao(imc):
    if imc < 18.5:
        return str('Abaixo do peso')
    elif 18.5 < imc < 24.9:
        return str('Peso normal')
    elif 25.0 < imc < 29.9:
        return str('Sobrepeso')
    elif imc > 30:
            return str('Obesidade')

for pessoa in range(lista_pessoas):
    peso_pessoa = float(input(f'Insira o peso da pessoa {pessoa + 1} (kg): '))
    altura_pessoa = float(input(f'Insira a altura da pessoa {pessoa +1} (metros): '))
    imc_pessoa = calcular_imc(peso_pessoa, altura_pessoa)
    classificacao = obter_classificacao(imc_pessoa)
    print(f'Seu IMC é: {imc_pessoa}.\nSua classificação é: {classificacao}.')

