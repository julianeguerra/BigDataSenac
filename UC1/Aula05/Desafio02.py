# contador = 0
# limite = 12

# while contador < limite:
#     try:
#         data_nascimento = int(input('Insira seu ano de nascimento'))
#         if data_nascimento > 2007:
#             print('Você não pode participar do programa')
#             break
#         else:
#             input('Nome: ')
#             input('Telefone: ')
#             input('E-mail: ')
#         contador = contador + 1
#     except: 
#         print('Valor inválido.')
contador_candidatos = 12
for candidato in range(contador_candidatos):
    try:
        ano_nascimento = int(input('Informe o ano de seu nascimento: '))
        ano_atual = 2025
        idade = ano_atual - ano_nascimento

        if idade < 18:
            print('Menores de 18 anos não podem participar do programa.')
            break
        elif idade >= 18:
            telefone =  input('Telefone: ')
            email = input('Email: ')
            contador_candidatos -= 1
            print('-'*40)
            print(f'Candidatura recebida. Obrigado! Sua candidatura:\n{telefone},\n{email}')
            print('-'*40)
        else:
            print('Informe um ano de nascimento válido.')
    except ValueError:
        print('ERRO: informe dados válidos.')
    except SyntaxError:
        print('ERRO: informe dados válidos.')