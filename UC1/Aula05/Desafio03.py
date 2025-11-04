usuario = 'admin'
senha = 123456
contador = 0
tentativas = 3

while contador < tentativas:
    try:
        print(f'Tentativas: {contador + 1} de {contador}')
        login_usuario = input('Insira o nome de usuário')
        senha_usuario = input('Insira a senha:')
        if login_usuario == usuario and senha_usuario == senha:
            print('Login bem-sucedido.')
            break
        else:
            print('Usuário ou senha inválidos. Tente novamente.')
            tentativas -= 1
            contador += 1
            print(f'Tentativas: {contador + 1} de {tentativas}')
    except ValueError:
            print('Valores incorretos inseridos')
if tentativas == 0:
    print('BLOQUEADO: número máximo de tentativas excedido.')