import random #Importa a biblioteca nativa random
# ------------------- Início do cardápio (lista de dicionário) --------------------
cardapio = [ 
        {
            "id": 1,
            "nome": "Sunomono",
            "descricao": "Salada de pepino japonês temperada com vinagre de arroz e gergelim.",
            "preco": 12.00
        },
        {
            "id": 2,
            "nome": "Guioza",
            "descricao": "Massa fina recheada com carne suína e legumes, grelhada e cozida no vapor.",
            "preco": 18.00
        },
        {
            "id": 3,
            "nome": "Shimeji na manteiga",
            "descricao": "Cogumelos refogados na manteiga e shoyu, servidos quentinhos.",
            "preco": 24.00
        },
        {
            "id": 4,
            "nome": "Combinado Sushi & Sashimi",
            "descricao": "8 sushis variados e 12 sashimis de salmão, atum e peixe branco.",
            "preco": 65.00
        },
        {
            "id": 5,
            "nome": "Sashimi de Salmão",
            "descricao": "12 fatias frescas de salmão, servidas com wasabi e gengibre.",
            "preco": 52.00
        },
        {
            "id": 6,
            "nome": "Uramaki Califórnia",
            "descricao": "Enrolado de arroz, kani, pepino e manga, com gergelim por fora.",
            "preco": 28.00
        }
] 
# ------------------ Fim do cardápio --------------------------
    
# -------------- Estrutura dos pedidos ------------------------ Com um pedido de exemplo
pedidos = [
    {
        "id": 1 ,
        "itens": [
            {              
                "idPrato": 6,
                "quantidade": 1,
            }
        ],
        "idMesa": 1
    }
]
# ----------------- Fim da estrutura dos pedidos ------------------
mesas = [1,2,3,4,5] # Número de mesas disponíveis

garcons = ['Júlio', 'Roberto', 'Mário', 'Janaína', 'Tereza'] # Garçons disponíveis


def mostrar_cardapio(): #Mostra os pratos do cardápio formatados linha a linha para o cliente escolher.
    print('----- CARDÁPIO DO TANOSHIMI-----')
    for item in cardapio:
        print(f"--- Prato {item['id']} ---\nNome: {item['nome']}\nDescrição: {item['descricao']}\nPreço: R$ {item['preco']}.")
        print('-'*80)
        
        
def fazer_pedido(): #Estrutura para o cliente fazer o pedido.
    pedido = {} #dicionário para armazenar o pedido final
    itens_pedidos = [] #lista para armazenar os itens escolhidos, opção e quantidade
    nao_terminou_escolher = True # Controle do loop
    
    mesas_disponiveis = print(f'As mesas disponíveis são: {mesas}.') #Exibe as mesas disponíveis
    pedido['idMesa'] = int(input('Escolha uma mesa. '))
    
    while True:
        try:
            if pedido['idMesa'] in mesas: # O código remove o número da mesa escolhido dos números disponíveis.
                mesas.remove(pedido['idMesa'])
                print(f"Mesa {pedido['idMesa']} escolhida com sucesso.")
                print('*'*80)
                break
            else:
                print('Mesa inválida! Tente outro número.')
                print(mesas_disponiveis)
        except ValueError:
            print('Digite apenas números.')
    mostrar_cardapio()
    
    while nao_terminou_escolher: #Loop para continuar perguntando ao cliente se ele quer pedir mais alguma coisa.
        try:
            opcao = int(input('Digite o número do prato: ')) #Pergunta ao cliente o número do prato
            quantidade = 0 #
            prato = None
            
            for item in cardapio: #Busca o prato no cardápio
                if item['id'] == opcao:
                    prato = item
                    break
                    
            if prato == None:
                print('Prato não existe, insira um número da lista.') #Tratamento se o número do prato não existir e reexibição do cardápio.
                mostrar_cardapio()
            
            else:
                try:
                    while quantidade == 0:
                        quantidade = int(input('Qual a quantidade? ')) #Pergunta a quantidade e cria um dicionário com id e quantidade e adiciona à lista itens_pedidos.
                        if quantidade == 0:
                            print('Quantidade não pode ser zero.')
                            
                    itens_pedidos.append({              
                        "idPrato": opcao,
                        "quantidade": quantidade,
                    })
                    
                    if input('Deseja adicionar mais um item? Sim ou Não: ').strip().lower() == "não": #Pergunta se quer adicionar mais itens. Se a resposta for não, sai do loop.
                        nao_terminou_escolher = False      
                
                except ValueError:
                    print('ERRO: insira um valor válido.')                    
        except ValueError:
            print('ERRO: insira um número válido.')
            
    pedido['itens'] = itens_pedidos #Adiciona a lista ao dicionários
    
            
    
    pedido['id'] = random.randint(100, 1000) #Gera um número de pedido aleatório.
    pedidos.append(pedido) #Adiciona o pedido à lista pedidos
    
    
    print('*'*40)
    print(f"Seu pedido é {pedido['id']}. Seu garçom é {random.choice(garcons)}.")
    print('*'*40)
    
def calculo_pedidos(quantidade, preco): # Função para calcular o preço do item vezes a quantidade.
    return quantidade * preco

def calcular_conta(id_pedido): #Função para calcular a conta com os pedidos adicionados e suas respectivas quantidades.
    total = 0
    for pedido in pedidos: #Procura pedido em pedidos com a ID correspondente
        if pedido['id'] == id_pedido: 
            for item in pedido['itens']:
                for prato in cardapio:
                    if prato['id'] == item['idPrato']: #Compara a ID do prato para encontrar o prato correspondente
                        total += calculo_pedidos(item['quantidade'], prato['preco']) #Faz o cálculo dos itens
    
    return total                    


nao_fez_todos_pedidos = True #Chama o input de fazer outro pedido enquanto o usuário não digitar "Não"

while nao_fez_todos_pedidos:
    try:
        fazer_pedido()
        nao_fez_todos_pedidos = input('Quer fazer outro pedido? Sim ou Não: ').strip().lower() == 'sim'
    except ValueError:
        print('ERRO: insira uma resposta válida.')

nao_pagou_todos = True #Loop de pagamento dos pedidos

while nao_pagou_todos:
    try:
        id_pedido = int(input('Digite o numero do pedido para pagamento: '))
        
        print(f'Você deve: R$ {calcular_conta(id_pedido):.2f}')
        
        nao_pagou_todos = input('Quer pagar outro pedido? Sim ou Não: ').strip().lower() == 'sim'
    except  ValueError:
        print('ERRO: insira um número válido.')