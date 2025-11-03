login = 'admin'
senha = 123456

contador = 0
limite = 3
try:
    senha_usuario = input('Insira o nome de usuário')
    senha_usuario = input('Insira a senha:')
    if senha_usuario != senha:
        contador - 1
    elif senha_usuario == senha:
        print('Login bem-sucedido.')
except:
        print('Valores incorretos inseridos')