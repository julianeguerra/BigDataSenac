#AULA 01 - Váriaveis em PYTHON (22/10/25)

## Categorias:

idade = 30 #int
nome = "Maria" #string
preco = 19.99 #float
estoque = True #boolean
estoque_disponivel = None #null

# Para rodar no terminal
## cd escolhe o diretório: cd Aula01
## para voltar para o diretório anterior: cd ..
## use 'ls' para ver tudo que tem no diretório
## use 'py' + nome do arquivo para rodar o arquivo depois de abrir a pasta: py aula01.py

print(idade)
print(type(idade))
print(nome)
print(type(nome))
print(preco)
print(type(preco))
print(estoque)
print(type(estoque))
print(estoque_disponivel)
print(type(estoque_disponivel))

#use input para receber uma informação do usuário
cadastro = input('Digite seu nome: ')
print(cadastro)
print(type(cadastro))

#use o nome do tipo de variável antes do input para definir o tipo de valor que será recebido:
numero = int(input('Digite um número: '))
print(numero)
print(type(numero))
