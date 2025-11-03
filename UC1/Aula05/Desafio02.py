contador = 0
limite = 12

while contador < limite:
    try:
        data_nascimento = int(input('Insira seu ano de nascimento'))
        if data_nascimento > 2007:
            print('Você não pode participar do programa')
            break
        else:
            input('Nome: ')
            input('Telefone: ')
            input('E-mail: ')
        contador = contador + 1
    except: 
        print('Valor inválido.')