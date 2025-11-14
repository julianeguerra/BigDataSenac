import random

# ------------------- Cardápio --------------------
cardapio = [ 
    {"id": 1, "nome": "Sunomono", "descricao": "Salada de pepino japonês temperada com vinagre de arroz e gergelim.", "preco": 12.00},
    {"id": 2, "nome": "Guioza", "descricao": "Massa fina recheada com carne suína e legumes, grelhada e cozida no vapor.", "preco": 18.00},
    {"id": 3, "nome": "Shimeji na manteiga", "descricao": "Cogumelos refogados na manteiga e shoyu, servidos quentinhos.", "preco": 24.00},
    {"id": 4, "nome": "Combinado Sushi & Sashimi", "descricao": "8 sushis variados e 12 sashimis de salmão, atum e peixe branco.", "preco": 65.00},
    {"id": 5, "nome": "Sashimi de Salmão", "descricao": "12 fatias frescas de salmão, servidas com wasabi e gengibre.", "preco": 52.00},
    {"id": 6, "nome": "Uramaki Califórnia", "descricao": "Enrolado de arroz, kani, pepino e manga, com gergelim por fora.", "preco": 28.00}
] 

pedidos = []
mesas = [1,2,3,4,5]
garcons = ['Júlio', 'Roberto', 'Mário', 'Janaína', 'Tereza']

# ---------------- Funções utilitárias ----------------
def pergunta_sim_ou_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ["sim", "não"]:
            return resposta
        print("ERRO: digite apenas 'Sim' ou 'Não'.")

def input_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("ERRO: insira um número válido.")

def buscar_prato_por_id(id_prato):
    return next((item for item in cardapio if item['id'] == id_prato), None)

# ---------------- Funções principais ----------------
def mostrar_cardapio():
    print('----- CARDÁPIO DO TANOSHIMI -----')
    for item in cardapio:
        print(f"--- Prato {item['id']} ---\nNome: {item['nome']}\nDescrição: {item['descricao']}\nPreço: R$ {item['preco']:.2f}")
        print('-'*80)

def escolher_mesa():
    print(f'Mesas disponíveis: {mesas}')
    while True:
        mesa = input_numero("Escolha uma mesa: ")
        if mesa in mesas:
            mesas.remove(mesa)
            print(f"Mesa {mesa} escolhida com sucesso.")
            return mesa
        print("Mesa inválida! Tente novamente.")

def adicionar_item():
    while True:
        opcao = input_numero("Digite o número do prato: ")
        prato = buscar_prato_por_id(opcao)
        if not prato:
            print("Prato não existe. Escolha novamente.")
            mostrar_cardapio()
            continue
        
        quantidade = 0
        while quantidade <= 0:
            quantidade = input_numero("Qual a quantidade? ")
            if quantidade <= 0:
                print("Quantidade deve ser maior que zero.")
        
        return {"idPrato": opcao, "quantidade": quantidade}

def fazer_pedido():
    pedido = {"idMesa": escolher_mesa(), "itens": []}
    mostrar_cardapio()
    
    while True:
        pedido["itens"].append(adicionar_item())
        if pergunta_sim_ou_nao("Deseja adicionar mais um item? Sim ou Não: ") == "não":
            break
    
    pedido["id"] = random.randint(100, 1000)
    pedidos.append(pedido)
    
    print('*'*40)
    print(f"Seu pedido é {pedido['id']}. Seu garçom será {random.choice(garcons)}.")
    print('*'*40)

def calcular_conta(id_pedido):
    pedido = next((p for p in pedidos if p['id'] == id_pedido), None)
    if not pedido:
        print("Pedido não encontrado.")
        return 0
    return sum(
        item['quantidade'] * buscar_prato_por_id(item['idPrato'])['preco']
        for item in pedido['itens']
    )

# ---------------- Fluxo principal ----------------
while True:
    fazer_pedido()
    if pergunta_sim_ou_nao("Quer fazer outro pedido? Sim ou Não: ") == "não":
        break

while True:
    id_pedido = input_numero("Digite o número do pedido para pagamento: ")
    total = calcular_conta(id_pedido)
    if total > 0:
        print(f"Você deve: R$ {total:.2f}")
    if pergunta_sim_ou_nao("Quer pagar outro pedido? Sim ou Não: ") == "não":
        break
