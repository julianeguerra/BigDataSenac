# 2. ADIVINHE O NÚMERO
# TEMA PRINCIPAL: Repetição (FOR) e Decisão (BREAK)
# LÓGICA: O jogador tem um número fixo de tentativas para acertar o valor.
# ------------------------------------------------------------------------------
print("\n--- 2. ADIVINHE O NÚMERO ---")
NUMERO_SECRETO = 42
TENTATIVAS_MAX = 5
# 1. Use um laço FOR para limitar as TENTATIVAS_MAX.
# 2. Dentro do loop, leia o palpite.
# 3. Use IF/ELIF/ELSE para dar dicas (MAIOR ou MENOR).
# 4. Se acertar, use o comando 'break' e imprima sucesso.


for tentativas in range(TENTATIVAS_MAX):
    try:
        numero = float(input('Insira um número: '))
        if numero > NUMERO_SECRETO:
            print('Tente um número menor.')
            print(f'Tentativas restantes: {TENTATIVAS_MAX - (tentativas + 1)}')
            print('*'*40)
        elif numero < NUMERO_SECRETO:
            print('Tente um número maior.')
            print(f'Tentativas restantes: {TENTATIVAS_MAX - (tentativas + 1)}')
            print('*'*40)
        elif numero == NUMERO_SECRETO:
            print('Você acertou. Parabéns!')
            break
        else:
            print('Insira um número.')
    except ValueError:
        print('ERRO: insira um número.')