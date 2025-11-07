# 1. VALIDADOR DE UM TRIÂNGULO
# TEMA PRINCIPAL: Decisão (If/elif/else)
# LÓGICA: A soma do comprimento de dois lados deve ser sempre maior que o terceiro. Isso define o que é um triângulo.
# ------------------------------------------------------------------------------
print("\n--- 1. VALIDADOR DE TRIÂNGULO ---")
# 1. Leia 3 lados (A, B, C)
# 2. Use IF/ELSE para verificar a condição de existência do triângulo.
# 3. Imprima se é ou não um triângulo válido.
try:
    a = float(input('Insira o comprimento do lado A: '))
    b = float(input('Insira o comprimento do lado B: '))
    c = float(input('Insira o comprimento do lado C: '))

    if (a + b > c) and (a + c > b) and (c + b > a):
        print('É um triangulo válido')
    else:
        print('Não é um triângulo válido.')
except ValueError:
    print('ERRO: insira um número válido.')