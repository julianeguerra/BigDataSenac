import random
# ------------------- Início do cardápio (dicionário) --------------------
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
    
# -------------- Estrutura dos pedidos ------------------------
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
mesas = [1,2,3,4,5]

garcons = [1,2,3,4,5]


def mostrar_cardapio(): #Mostra os pratos do cardápio formatados linha a linha para o cliente escolher.
    print('----- CARDÁPIO DO TANOSHIMI-----')
    for item in cardapio:
        print(f"--- Prato {item['id']} ---\nNome: {item['nome']}\nDescrição: {item['descricao']}\nPreço: R$ {item['preco']}.")
        
        
def fazer_pedido(): #Estrutura para o cliente fazer o pedido.
    pedido = {}
    itens_pedidos = []
    nao_terminou_escolher = True
    
    while nao_terminou_escolher: #Loop para continuar perguntando ao cliente se ele quer pedir mais alguma coisa.
        try:
            opcao = int(input('Digite o número do prato (ou 0 para encerrar): '))
            quantidade = 0
            prato = None
            
            for item in cardapio:
                if item['id'] == opcao:
                    prato = item
                    break
                    
            if prato == None:
                print('Prato não existe, insira um número da lista')
                mostrar_cardapio()
            
            else:
                while quantidade == 0:
                    quantidade = int(input('Qual a quantidade?')) #Cria um dicionário com id e quantidade e adiciona à lista itens_pedidos.
                    if quantidade == 0:
                        print('Quantidade não pode ser zero.')
                        
                itens_pedidos.append({              
                    "idPrato": opcao,
                    "quantidade": quantidade,
                })
                
                if input('Deseja adicionar mais um item? Sim ou Não. ').strip().lower() == "não":
                    nao_terminou_escolher = False      

        except ValueError:
            print('ERRO: insira um número válido.')
            
    pedido['itens'] = itens_pedidos
    mesas_disponiveis = print(f'As mesas disponíveis são: {mesas}.')
    pedido['idMesa'] = int(input('Qual o número da mesa? '))
    
    if pedido['idMesa'] in mesas: # O código deve remover o número da mesa escolhido dos números disponíveis
        mesas.remove(pedido['idMesa'])
    
    pedido['id'] = random.randint(100, 1000) 
    pedidos.append(pedido)
    
    print(f'Seu pedido é {pedido['id']}')
    
def calculo_pedidos(quantidade, preco): # confirmar se é válido. A função depois vai calcular o preço do item e quantidade.
    return quantidade * preco

def calcular_conta(id_pedido):
    total = 0
    for pedido in pedidos:
        if pedido['id'] == id_pedido:
            for item in pedido['itens']:
                for prato in cardapio:
                    if prato['id'] == item['idPrato']:
                        total += calculo_pedidos(item['quantidade'], prato['preco'])
    
    return total                    

mostrar_cardapio()

nao_fez_todos_pedidos = True

while nao_fez_todos_pedidos:
    fazer_pedido()
    nao_fez_todos_pedidos = input('Deseja fazer outro pedido? Sim ou Não').strip().lower() == 'sim'

nao_pagou_todos = True

while nao_pagou_todos:
    id_pedido = int(input('Digite o numero do pedido que deseja pagar: '))
    
    print(f'Você deve: R$ {calcular_conta(id_pedido):.2f}')
    
    nao_pagou_todos = input('Deseja pagar outro pedido? Sim ou Não').strip().lower() == 'sim'
    
    
                
    