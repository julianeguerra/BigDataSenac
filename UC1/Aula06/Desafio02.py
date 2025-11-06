contador_candidatos = 5
candidatos_validos = []
for candidato in range(contador_candidatos):
    try:
        ano_nascimento = int(input('Informe o ano de seu nascimento: '))
        ano_atual = 2025
        idade = ano_atual - ano_nascimento

        if idade < 18:
            print('Menores de 18 anos não podem participar do programa.')
            break
        elif idade >= 18:
            nome = input('Nome: ')
            telefone =  input('Telefone: ')
            email = input('Email: ')
            contador_candidatos -= 1
            print('-'*40)
            print(f'Candidatura recebida. Obrigado! Sua candidatura:\n{nome}\n{telefone},\n{email}')
            print('-'*40)
            candidato = {
                'nome': nome,
                'telefone': telefone,
                'email': email
            }
            candidatos_validos.append(candidato)
        else:
            print('Informe um ano de nascimento válido.')
    except ValueError:
        print('ERRO: informe dados válidos.')
    except SyntaxError:
        print('ERRO: informe dados válidos.')

for candidato in candidatos_validos:
    print(candidato)